from typing import Tuple, Union, List

from sql_smith.interfaces import ExpressionInterface, StatementInterface
from sql_smith.partial import Expression, QualifiedIdentifier, Identifier, Literal, Listing, Criteria
from sql_smith.partial.parameter import Parameter


def __is_statement(value) -> bool:
    return isinstance(value, StatementInterface)


def param(value) -> 'StatementInterface':
    """Create a parameter.

    >>> func('POINT', param(1), param(2))  # POINT(? , ?)
    """
    if __is_statement(value):
        return value
    return Parameter.create(value)


def param_all(*values):
    return tuple(map(param, values))


def express(pattern: str, *args):
    """Create an expression.

    >>> express('{} + 1', identify('visit'))  # "visit" + 1
    """
    return Expression(pattern, *param_all(*args))


def alias(field_name, field_alias: str) -> 'ExpressionInterface':
    """Create an alias for a column or a function.

    >>> alias('users.id', 'uid')  # "users"."id" AS "uid"
    """
    return express('{} AS {}', identify(field_name), identify(field_alias))


def listing(values: Union[Tuple, List], separator: str = ', ') -> Listing:
    """Create a listing.

    >>> listing((1, 1, 2, 3, 5))  # ?, ?, ?, ?, ?
    >>> listing(identify_all('id', 'username', 'email'))  # "id", "username", "email"
    """
    return Listing(separator, *param_all(*values))


def func(function: str, *args) -> 'ExpressionInterface':
    """Create a function.

    >>> func('COUNT', 'user.id')  # COUNT("users"."id")
    """
    return express('{}({{}})'.format(function), listing(identify_all(*args)))


def literal(value) -> 'StatementInterface':
    """Create a literal.
    """
    if __is_statement(value):
        return value
    return Literal(value)


def criteria(pattern: str, *args) -> 'CriteriaInterface':
    """Create a criteria.

    >>> c = criteria(
    >>>     "{} = {}",
    >>>     func(
    >>>         'YEAR',
    >>>         identify('start_date')
    >>>     ),
    >>>     literal(2021)
    >>> )  # YEAR("start_date") = 2021
    """
    return Criteria(express(pattern, *args))


def on(left: str, right: str):
    """Create an on clause.
    """
    return criteria('{} = {}', identify(left), identify(right))


def order(column, direction: str = None) -> 'StatementInterface':
    """Create an order clause."""
    if direction is None:
        return identify(column)
    return express('{{}} {}'.format(direction.upper()), identify(column))


def group(c: 'CriteriaInterface') -> 'CriteriaInterface':
    """Create a group of criteria.

    >>> group(
    >>>     field('username').eq('tom')
    >>>     .or_(field('first_name').eq('Tom'))
    >>> ).and_(
    >>>     field('is_active').eq(1)
    >>> )
    >>> # ("username" = ? OR "first_name" = ?) AND "is_active" = ?
    """
    return criteria('({})', c)


def field(name):
    """Starts a criteria for a column. Use it to create a condition.

    >>> field('users.id').eq(100)  # "users".id = ?
    """
    from sql_smith.builder import CriteriaBuilder
    return CriteriaBuilder(identify(name))


def search(name):
    """Start a LIKE clause.

    >>> search('username').contains('admin')  # "username" LIKE '%admin%'
    """
    from sql_smith.builder import LikeBuilder
    return LikeBuilder(identify(name))


def identify_all(*names) -> Tuple:
    """Identify all names.

    >>> identify_all('id', 'username')  # ("id", "username")
    """
    return tuple(map(identify, names))


def identify(name) -> 'StatementInterface':
    """Identify a name.

    >>> identify('users.id')  # "users"."id"
    """
    if __is_statement(name):
        return name

    if name.find('.') != -1:
        return QualifiedIdentifier(*identify_all(*name.split('.')))

    if name == '*':
        return Literal(name)

    return Identifier(name)

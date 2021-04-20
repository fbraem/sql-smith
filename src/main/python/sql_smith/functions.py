from typing import Tuple, Union, List

from sql_smith.interfaces import ExpressionInterface, StatementInterface
from sql_smith.partial import Expression, QualifiedIdentifier, Identifier, Literal, Listing, Criteria
from sql_smith.partial.parameter import Parameter


def __is_statement(value) -> bool:
    return isinstance(value, StatementInterface)


def param(value) -> 'StatementInterface':
    if __is_statement(value):
        return value
    return Parameter.create(value)


def param_all(*values):
    return tuple(map(param, values))


def express(pattern: str, *args):
    return Expression(pattern, *param_all(*args))


def alias(field_name, field_alias: str) -> 'ExpressionInterface':
    """Create an alias for a column or a function"""
    return express('{} AS {}', identify(field_name), identify(field_alias))


def listing(values: Union[Tuple, List], separator: str = ', ') -> Listing:
    return Listing(separator, *param_all(*values))


def func(function: str, *args) -> 'ExpressionInterface':
    return express('{}({{}})'.format(function), listing(identify_all(*args)))


def literal(value) -> 'StatementInterface':
    if __is_statement(value):
        return value
    return Literal(value)


def criteria(pattern: str, *args) -> 'CriteriaInterface':
    return Criteria(express(pattern, *args))


def on(left: str, right: str):
    return criteria('{} = {}', identify(left), identify(right))


def order(column, direction: str = None) -> 'StatementInterface':
    if direction is None:
        return identify(column)
    return express('{{}} {}'.format(direction.upper()), identify(column))


def group(c: 'CriteriaInterface') -> 'CriteriaInterface':
    return criteria('({})', c)


def field(name):
    from sql_smith.builder import CriteriaBuilder
    return CriteriaBuilder(identify(name))


def search(name):
    from sql_smith.builder import LikeBuilder
    return LikeBuilder(identify(name))


def identify_all(*names) -> Tuple:
    return tuple(map(identify, names))


def identify(name) -> 'StatementInterface':
    if __is_statement(name):
        return name

    if name.find('.') != -1:
        return QualifiedIdentifier(*identify_all(*name.split('.')))

    if name == '*':
        return Literal(name)

    return Identifier(name)

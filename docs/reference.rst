=========
Reference
=========
All the following functions are defined in the functions module.

Criteria
********

field
-----
Use field when a column is needed in a criteria.

.. code-block:: python

    field('users.id').eq(100)  # "users".id = ?
    field('users.birthday').lt('2000-01-01')  # "users"."birthday" > ?
    field('users.last_login').between(yesterday, today)  # "users"."last_login" BETWEEN ? AND ?
    field('users.role').not_in('admin', 'moderator')  # "users"."role" NOT IN (?, ?)
    field('countries.id').in_(select)  # "countries"."id" IN (?)
    field('total').gt(9000)  # "total" > ?
    field('salary').lte(3000)  # "salary" <= ?
    field('deleted_at').is_null()  # "deleted_at" IS NULL
    field('parent_id').is_not_null()  # "parent_id" IS NOT NULL

search
------
Use search for LIKE.

.. code-block:: python

    search('username').contains('admin')  # "username" LIKE '%admin%'
    search('first_name').begins('john')  # "firstname" LIKE 'john%'
    search('last_name').not_ends('rump')  # "last_name" NOT LIKE '%rump' 

on
---
on can be used in conjunction with join.

.. code-block:: python

    on('countries.id', 'users.country_id')  # "countries"."id" = "users"."country_id"

group
-----
Use group to combine criteria

.. code-block:: python

    group(
        field('username').eq('tom') \
        .or_(field('first_name').eq('Tom'))
    ).and_(
        field('is_active').eq(1)
    )
    # ("username" = ? OR "first_name" = ?) AND "is_active" = ?

Expressions
***********

express
-------
All expressions are written with the print format, where any {} will be replaced with anything that
implement the StatementInterface (like queries and other expressions).

.. code-block:: python

    express('{} <= NOW()', identify('execute_at'))  #  "execute_at" <= NOW()
    express('{} + 1', identify('number_of_views'))  # "number_of_views" + 1

Aliases
*******

alias
-----
Create an alias for a column or an expression with alias.

.. code-block:: python

    alias('users.id', 'uid')  # "users"."id" AS "uid"

Functions
*********

func
____
Use func for functions.

.. code-block:: python

    func('COUNT', 'user.id')  # COUNT("users"."id")
    func('CONCAT', 'first_name', 'last_name')  # CONCAT("first_name", "last_name")
    
By default functions assume identifiers as parameters, use param for scalar values:

.. code-block:: python

    func('POINT', param(1), param(2))  # POINT(? , ?)

Identifiers
***********

identifier
----------
.. code-block:: python

    identify('users.username')  # "users"."username"
    identify('country')  # "country"

identifier_all
--------------
.. code-block:: python

    identify_all('id', 'username')  # ("id", "username")

Lists
*****

listing
-------
.. code-block:: python

    listing((1, 1, 2, 3, 5))  # ?, ?, ?, ?, ?
    listing(identify_all('id', 'username', 'email'))  # "id", "username", "email"

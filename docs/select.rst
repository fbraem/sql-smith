======
SELECT
======

Use :py:func:`~sql_smith.QueryFactory.select` of :py:class:`~sql_smith.QueryFactory` to create a SELECT statement.
The return value is an instance of :py:class:`~sql_smith.query.SelectQuery`.

.. code-block:: python

    factory = QueryFactory(CommonEngine())
    query = factory \
        .select() \
        .from_('users') \
        .limit(100) \
        .compile()

    print(query.sql)  # SELECT * FROM "users" LIMIT 100
    print(query.params)  # ()


Specific columns can be selected:

.. code-block:: python

    query = factory \
        .select('id', 'username') \
        .from_('users') \
        .compile()

    print(query.sql)  # SELECT "id", "username" FROM "users"
    print(query.params)  # ()

additional columns can be added:

.. code-block:: python

    query = factory \
        .select('id', 'username') \
        .add_columns('password') \
        .from_('users') \
        .compile()

    print(query.sql)  # SELECT "id", "username", "password" FROM "users"
    print(query.params)  # ()

As well as additional tables:

.. code-block:: python

    query = factory \
        .select('users.username', 'groups.name') \
        .from_('users') \
        .add_from('groups') \
        .compile()

    print(query.sql)  # SELECT "users"."username", "groups"."name" FROM "users", "groups"
    print(query.params)  # ()

WHERE
*****
Apply criteria to a WHERE condition:

.. code-block:: python

    query = factory \
        .select() \
        .from_('countries') \
        .where(field('language')->eq('EN')) \
        .compile()

    print(query.sql)  # SELECT * FROM "countries" WHERE "language" = ?
    print(query.params)  # ('EN', )

Additional criteria can be added using and_where and or_where

.. code-block:: python

    query = factory \
        .select() \
        .from_('users') \
        .where(field('id')->gt(1)) \
        .or_where(field('login_at')->is_null()) \
        .or_where(field('is_inactive')->eq(1)) \
        .compile()

    print(query.sql)  # SELECT * FROM "users" WHERE "id" > ? OR "login_at" IS NULL OR "is_inactive" > ?
    print(query.params)  # (1, 1)

JOIN
*****
Joins are added in a similar way:

.. code-block:: python

    query = factory \
        .select('u.id', 'c.name') \
        .from_(alias('users', 'u')) \
        .join(alias('countries', 'c'), on('u.country_id', 'c.id')) \
        .compile()

    print(query.sql)  # SELECT * FROM "users" AS "u" JOIN "countries" AS "c" ON "u"."country_id" = "c"."id"
    print(query.params)  # ()

The join type can be specified as third parameter of join or one of these helpers can be used for
common types:

+ left_join
+ right_join
+ inner_join
+ full_join

ORDER BY
********
Ordering can be applied:

.. code-block:: python

    factory = QueryFactory(CommonEngine())
    query = factory \
        .select() \
        .from_('users') \
        .order_by('username', 'asc') \
        .compile()

    print(query.sql)  # SELECT * FROM "users" ORDER BY "username" DESC
    print(query.params)  # ()
    
ordering can be reset by omitting the order column:

.. code-block:: python

    query.order_by()


LIMIT and OFFSET
****************
Limits and offsets can be applied:

.. code-block:: python

    factory = QueryFactory(CommonEngine())
    query = factory \
        .select() \
        .from_('posts') \
        .offset(10)
        .limit(10)
        .compile()

    print(query.sql)  # SELECT * FROM "posts" OFFSET 10 LIMIT 10
    print(query.params)  # ()
    
.. note::
   When using the SQL Server engine an offset must be defined for the limit to be applied! Use
   offset(0) when no offset is required.

GROUP BY
********
Grouping can be applied:

.. code-block:: python

    query = self._factory \
        .select(
            alias(func('COUNT', 'id'), 'total')
        ) \
        .from_('employees') \
        .group_by('department') \
        .compile()

    print(query.sql)  # SELECT COUNT("id") AS "total" FROM "employees" GROUP BY "department"
    print(query.param)  # ()

And also the having clause can be applied:

.. code-block:: python

    salary_sum = func('SUM', 'salary')
    query = self._factory \
        .select(
            'department',
            alias(salary_sum, 'total')
        ) \
        .from_('employees') \
        .group_by('department') \
        .having(field(salary_sum).gt(5000))

        print(query.sql)  # SELECT "department", SUM("salary") AS "total" FROM "employees" GROUP BY "department" HAVING SUM("salary") > ?
        print(query.params)  # (5000, )


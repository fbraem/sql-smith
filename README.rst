=========
sql-smith
=========

**sql-smith** is an SQL query builder with zero dependencies and a fluent interface.

    The sentence above is, beside the name, a copy from the website of the PHP library
    Latitude_, for the simple reason that this Python module is a port of Latitude.

Installation
------------

.. code-block:: sh
    $ pip install sql-smith

Quick Start
-----------

.. code-block:: python
    from sql_smith import QueryFactory
    from sql_smith.engine import CommonEngine
    from sql_smith.functions import field
    
    factory = QueryFactory(CommonEngine())
    query = factory
        .select('id', 'username')
        .from_('users')
        .where(field('id').eq(5))
        .compile()
    
    print(query.sql)  # SELECT "id" FROM "users" WHERE "id" = ?
    print(query.params)  # (5)

.. _Latitude: https://latitude.shadowhand.com/

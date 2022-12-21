=========
sql-smith
=========

**sql-smith** is an SQL query builder with zero dependencies and a fluent interface.

    The sentence above is, beside the name, a copy from the website of the PHP library
    Latitude_, for the simple reason that this Python module is a port of Latitude.

Read the full `documentation <https://fbraem.github.io/sql-smith>`_.

Installation
************

.. code-block:: sh

    $ pip install sql-smith

Quick Start
***********

QueryFactory is a factory to create a **SELECT**, **INSERT**, **UPDATE** or **DELETE** query.
Use the fluent interface of the queries to complete the query.

.. code-block:: python

    from sql_smith import QueryFactory
    from sql_smith.engine import CommonEngine
    from sql_smith.functions import field
    
    factory = QueryFactory(CommonEngine())
    query = factory \
        .select('id', 'username') \
        .from_('users') \
        .where(field('id').eq(5)) \
        .compile()
    
    print(query.sql)  # SELECT "id", "username" FROM "users" WHERE "id" = ?
    print(query.params)  # (5)

When the query is ready, compile it. The return value of compile is a Query class instance
with two properties: sql and params. Use these properties to pass the query to a database.

.. code-block:: python

    import sqlite3
    
    db = sqlite3.connect('test.db')
    cur = db.cursor()

    for row in cur.execute(query.sql, query.params):
        print(row)

Acknowledgment
==============
Big thanks to JetBrains_ to let me use PyCharm for free!

.. _Latitude: https://latitude.shadowhand.com/
.. _JetBrains: https://www.jetbrains.com/pycharm/

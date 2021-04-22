Quick Start
===========

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

:py:class:`~sql_smith.QueryFactory` is a factory to create a **SELECT**, **INSERT**, **UPDATE** or **DELETE** query.
Use the fluent interface of the queries to complete the query.

When the query is ready, compile it. The return value of compile is a :py:class:`~sql_smith.query.Query` class instance
with two properties: sql and params. Use these properties to pass the query to a database.

.. code-block:: python

    import sqlite3
    
    db = sqlite3.connect('test.db')
    cur = db.cursor()

    for row in cur.execute(query.sql, query.params):
        print(row)

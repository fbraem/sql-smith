======
INSERT
======

Use the :py:func:`~sql_smith.QueryFactory.insert` method of :py:class:`~sql_smith.QueryFactory` to create 
an INSERT statement. The return value is an instance of :py:class:`~sql_smith.query.InsertQuery`.

Inserts can be performed with a single row:

.. code-block:: python

    factory = QueryFactory(CommonEngine())
    query = factory \
        .insert(
            'places', 
            {
                'name': 'home',
                'address': '123 Main St'
            }
        ) \
        .compile()

    print(query.sql)  # INSERT INTO "places" ("name", "address") VALUES (?, ?)
    print(query.params);  # ('home', '123 Main St')

or multiple rows:

.. code-block:: python

    insert = self._factory \
        .insert('users') \
        .columns('id', 'username') \
        .values(2, 'jenny') \
        .values(3, 'rick') \
        .compile()

    print(query.sql)  # INSERT INTO "users" ("id", "username") VALUES (?, ?), (?, ?)
    print(query.params)  # (2, 'jenny', 3, 'rick')

When using the Postgres engine RETURNING can be added:

.. code-block:: python

    factory = QueryFactory(PostgresEngine())
    query = factory \
        .insert(
            'friends', 
            {
                'user_id': 11,
                'friend_id': 30
            }
        ) \
        .returning('id') \
        .compile()

    print(query.sql)  # INSERT INTO "friends" ("user_id", "friend_id") VALUES (?, ?) RETURNING "id"
    print(query.params)  # (11, 30)

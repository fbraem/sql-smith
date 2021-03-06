======
UPDATE
======

Use the :py:func:`~sql_smith.QueryFactory.update` method of :py:class:`~sql_smith.QueryFactory` to create an UPDATE
statement. The return value is an instance of :py:class:`~sql_smith.query.UpdateQuery`.

.. code-block:: python

    factory = QueryFactory(CommonEngine())
    query = factory \
        .update(
            'places', 
            {
                'address' => '555 Money Ave'
            }
        ) \
        .where(field('name').eq('work')) \
        .compile()

    print(query.sql)  # UPDATE "places" SET "address" = ? WHERE "name" = ?
    print(query.params)  # ('555 Money Ave', 'work')

When using the Postgres engine, RETURNING can be added:

.. code-block:: python

    factory = QueryFactory(PostgresEngine())
    query = factory \
        .update(
            'users', 
            {
                'is_active': False
            }
        ) \
        .where(field('login_at')->lt('2018-01-01'))
        .returning('id') \
        .compile()

    print(query.sql)  # UPDATE "users" SET "is_active" = false WHERE "login_at" < ? RETURNING "id"
    print(query.params)  # ('2018-01-01', )

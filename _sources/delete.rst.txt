======
DELETE
======

Use the :py:func:`~sql_smith.QueryFactory.delete` method of :py:class:`~sql_smith.QueryFactory` to create a DELETE 
statement. The return value is an instance of :py:class:`~sql_smith.query.DeleteQuery`.

.. code-block:: python

    factory = QueryFactory(CommonEngine())
    query = factory \
        .delete('users') \
        .where(field('login_at').is_null()) \
        .compile()

    print(query.sql)  # DELETE FROM "users" WHERE "login_at" IS NULL
    print(query.params)  # ()

It is also possible to provide a LIMIT:

.. code-block:: python

    factory = QueryFactory(CommonEngine())
    query = factory \
        .delete('users') \
        .limit(5) \
        .compile()

    print(query.sql)  # DELETE FROM "users" LIMIT 5
    print(query.params)  # ()

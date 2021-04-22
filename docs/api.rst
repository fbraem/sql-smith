===
API
===

A developer building SQL statements only needs to create a QueryFactory with the desired engine. Assemble the
query with the available functions and compile it to get the SQL statement as a string and the parameters as
a tuple.

.. module:: sql_smith

Engines
*******

An engine is responsible for creating query instances. These methods are called by the QueryFactory.
It also provides methods to handle common query builder actions (like escaping an identifier). When a database
needs an exception, a specific Engine class can derive from BasicEngine and implement the different behaviour.

.. autoclass:: sql_smith.engine.BasicEngine
    :members:

.. autoclass:: sql_smith.engine.CommonEngine
    :members:

.. autoclass:: sql_smith.engine.MysqlEngine
    :members:

.. autoclass:: sql_smith.engine.PostgresEngine
    :members:

.. autoclass:: sql_smith.engine.SqlServerEngine
    :members:

.. autoclass:: sql_smith.engine.SqliteEngine
    :members:

QueryFactory
************

The query factory is responsible for creating queries.

.. autoclass:: sql_smith.QueryFactory

Functions
*********

.. automodule:: sql_smith.functions
     :members:

Queries
*******

.. autoclass:: sql_smith.query.AbstractQuery
    :members:

.. autoclass:: sql_smith.query.DeleteQuery
    :members:

.. autoclass:: sql_smith.query.InsertQuery
    :members:

.. autoclass:: sql_smith.query.Query
    :members:

.. autoclass:: sql_smith.query.SelectQuery
    :members:

.. autoclass:: sql_smith.query.UnionQuery
    :members:

.. autoclass:: sql_smith.query.UpdateQuery
    :members:

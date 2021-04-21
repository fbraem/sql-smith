===
API
===

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

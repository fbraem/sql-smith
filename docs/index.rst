=========
sql-smith
=========

**sql-smith** is an SQL query builder with zero dependencies and a fluent interface.

    The sentence above is, beside the name, a copy from the website of the PHP library
    Latitude_, for the simple reason that this Python module is a port of Latitude.

Documentation
*************
sql-smith includes a query builder and a set of escaping helpers. The query builder allows the fluent generation of 
**SELECT**, **INSERT**, **UPDATE**, and **DELETE** statements. The escaping helpers assist in protecting against SQL 
injection and identifier quoting for MySQL, SQL Server, Postgres, and other databases that follow SQL standards.

.. toctree::
    :maxdepth: 2

    installation
    quickstart
    queries
    functions
    api
    difference

.. _Latitude: https://latitude.shadowhand.com/

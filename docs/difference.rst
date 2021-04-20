=====================
Latitude vs sql-smith
=====================

As said in the introduction, sql-smith is a port of the PHP library Latitude_. Due to the
differences between PHP and Python there are some differences in the implementation.

Python keywords
***************
**from**, **in**, **and** and **or** are keywords in Python. Keywords can't be used as method name.
The rule is to append an underscore to such method names. So from becomes from\_, in becomes in\_, ...

Parameters
**********
Parameters are tuples.

Naming conventions
******************
sql-smith uses PEP8. As a consequence, orWhere is named or_where for example.

.. _Latitude: https://latitude.shadowhand.com/

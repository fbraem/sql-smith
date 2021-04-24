#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.sphinx")
use_plugin("python.distutils")


name = "sql-smith"
version = "1.0.0"

summary = "sql-smith is an SQL query builder with zero dependencies and a fluent interface."
url = "https://github.com/fbraem/sql-smith"
authors = [Author("Franky Braem", "franky.braem@gmail.com")]
license = "MIT"

default_task = "publish"


@init
def set_properties(project):
    project.build_depends_on("pygments")

    # .coveragerc isn't used by the plugin, so disable break build for now.
    project.set_property("coverage_break_build", False)  # default is True

    project.set_property("flake8_verbose_output", True)

    project.set_property("distutils_readme_description", True)
    project.set_property("distutils_description_overwrite", True)
    project.set_property("distutils_readme_file", "README.rst")
    project.set_property("distutils_classifiers", [
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ])
    project.set_property("distutils_setup_keywords", [
        "sql-smith", "query", "builder", "querybuilder", "sql", "mysql", "sqlite", "postgres", "sqlserver", "database"
    ])
    project.set_property("distutils_upload_repository_key", "testpypi")

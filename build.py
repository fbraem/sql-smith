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



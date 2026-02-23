# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQuandary(PythonPackage):
    """Python interface for Quandary: Optimal control for open quantum systems"""

    homepage = "https://github.com/LLNL/quandary"
    git = "https://github.com/LLNL/quandary.git"

    maintainers("steffi7574", "tdrwenski", "adrienbernede")

    license("MIT", checked_by="tdrwenski")

    version("main", branch="main", preferred=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-scikit-build-core@0.4.3: +pyproject", type="build")
    depends_on("py-nanobind@2.1:", type="build")
    depends_on("cmake@3.23:", type="build")

    depends_on("quandary")
    depends_on("blt@0.6.0:", type="build")
    depends_on("tomlplusplus", type="build")

    depends_on("py-numpy@1.26:", type=("build", "run"))
    depends_on("py-mpi4py@3.1:", type=("build", "run"))

    def config_settings(self, spec, prefix):
        return {
            "cmake.define.BLT_SOURCE_DIR": str(spec["blt"].prefix),
            "cmake.define.BUILD_PYTHON_BINDINGS": "ON",
            "cmake.define.ENABLE_TESTS": "OFF",
        }

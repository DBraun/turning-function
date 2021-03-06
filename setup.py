import sys

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
from pathlib import Path

__version__ = "0.0.3"

ext_modules = [
    Pybind11Extension("turning_function",
        ["src/main.cpp"],
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        ),
]

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="turning_function",
    version=__version__,
    author="David Braun",
    author_email="braun@ccrma.stanford.edu",
    url="https://github.com/DBraun/turning-function",
    description="Python implementation of \"An efficiently computable metric for comparing polygonal shapes\" (Arkin et al.)",
    long_description=long_description,
    long_description_content_type='text/markdown',
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)

from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        'simple_ml_ext',
        ['src/simple_ml_ext.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++'
    ),
]

setup(
    name='simple_ml_ext',
    ext_modules=ext_modules,
)

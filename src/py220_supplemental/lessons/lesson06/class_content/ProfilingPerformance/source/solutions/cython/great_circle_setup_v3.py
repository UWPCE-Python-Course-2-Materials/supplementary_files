from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Great Circle v3',
    ext_modules=cythonize("great_circle_v3.pyx"),
)

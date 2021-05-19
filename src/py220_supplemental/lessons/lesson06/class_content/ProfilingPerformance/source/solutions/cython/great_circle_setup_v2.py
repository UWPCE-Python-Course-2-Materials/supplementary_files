from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Great Circle v2',
    ext_modules=cythonize("great_circle_v2.pyx"),
)

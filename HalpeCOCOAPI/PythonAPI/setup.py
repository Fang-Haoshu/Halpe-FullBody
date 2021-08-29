from setuptools import setup, Extension
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'halpecocotools._mask',
        sources=['common/maskApi.c', 'halpecocotools/_mask.pyx'],
        include_dirs = [np.get_include(), 'common'],
        extra_compile_args=[],
    )
]

setup(
    name='halpecocotools',
    packages = ['halpecocotools'],
    package_dir = {'halpecocotools': 'halpecocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0',
    ],
    version='0.0.0',
    description="COCO API for Halpe-Fullbody dataset",
    url="https://github.com/HaoyiZhu/HalpeCOCOAPI",
    ext_modules= ext_modules
)

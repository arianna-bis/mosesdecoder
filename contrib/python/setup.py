from distutils.core import setup
from distutils.extension import Extension
import os

mosesdir = os.path.abspath('../../')
includes = [mosesdir, os.path.join(mosesdir, 'moses/src'), os.path.join(mosesdir, 'util')]

libdir = os.path.join(mosesdir, 'lib')
basic=['z', 'stdc++', 'pthread', 'm', 'gcc_s', 'c', 'boost_system', 'boost_thread', 'boost_filesystem', 'rt', 'cmph']
moses=['OnDiskPt', 'kenutil', 'kenlm', 'LM', 'mert_lib', 'moses_internal', 'CYKPlusParser', 'Scope3Parser', 'fuzzy-match', 'RuleTable', 'CompactPT', 'moses', 'dynsa', 'pcfg_common' ]

exobj = [os.path.join(libdir, 'lib' + l + '.so') for l in moses]

ext_modules = [
    Extension(name = 'binpt',
        sources = ['binpt/binpt.cpp'],
        language = 'C++', 
        include_dirs = includes,
        extra_objects = exobj,
        library_dirs = [libdir],
        runtime_library_dirs = [libdir],
        libraries = basic + moses,
        extra_compile_args = ['-O3', '-DNDEBUG'],
    )
]

setup(
    name='binpt',
    ext_modules=ext_modules
)

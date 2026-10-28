from setuptools import setup
import os
import shutil

#remove the dist folder first if exists
if os.path.exists("dist"):
    shutil.rmtree("dist")

def readme():
	with open('README.rst') as f:
		return(f.read())

VERSION = '1.1.6'

def write_version_py(filename='sigProfilerPlotting/version.py'):
    # Copied from numpy setup.py
    cnt = """
# THIS FILE IS GENERATED FROM SIGPROFILERPLOTTING SETUP.PY
short_version = '%(version)s'
version = '%(version)s'
    
    """
    fh = open(filename, 'w')
    fh.write(cnt % {'version': VERSION,})
    fh.close()

write_version_py()

# Fonts: the bundled TTFs (repo-level fonts/) are packaged as the
# sigProfilerPlotting.fonts subpackage and registered with matplotlib at
# import time (see sigProfilerPlotting._register_bundled_fonts). The old
# custom install command that copied them into matplotlib's font directory
# and called the private font_manager._rebuild() (removed in matplotlib
# 3.6) is gone; it never ran for wheel-based installs anyway.

setup(name='sigProfilerPlotting',
		version=VERSION,
		description='SigProfiler plotting tool',
		url='',
		author='Erik Bergstrom',
		author_email='ebergstr@eng.ucsd.edu',
		license='UCSD',
		packages=['sigProfilerPlotting', 'sigProfilerPlotting.fonts'],
		# fonts/ lives at the repository root (docker/backend.dockerfile copies
		# it from there), so map it into the package instead of moving it.
		package_dir={'sigProfilerPlotting.fonts': 'fonts'},
		install_requires =[
			"matplotlib"],
		package_data={'sigProfilerPlotting.fonts': ['*.ttf']},
		include_package_data=True,
		zip_safe=False)


## this file is generated from settings in build.vel

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# from options["setup"] in build.vel
config = {
 'description': 'modargs is a simple command line argument parsing library that infers arguments from functions in a module',
 'author': 'Zed A. Shaw',
 'url': 'http://pypi.python.org/pypi/python-modargs',
 'download_url': 'http://pypi.python.org/pypi/python-modargs',
 'author_email': 'zedshaw@zedshaw.com',
 'version': '1.7',
 'packages': ['modargs'],
 'name': 'python-modargs'
}
setup(**config)


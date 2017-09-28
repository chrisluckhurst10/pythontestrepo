try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Template for python packages',
    'author': 'me',
    'author_email': "some-email@somesite.com",
    'install_requires': ['pytest>=1.0.0'],
    'packages': ['pythontest'],
    'name': 'pythonictest',
    'version': '0.0.2',
}

setup(**config)

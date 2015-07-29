try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Attempting to learn how to make GUIs with Python',
    'author': 'Nick P.',
    'url': 'https://github.com/npiscitello/PythonGUI',
    'download_url': 'Where to download it.',
    'author_email': 'nb.piscitello+python@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'PythonGUI'
}

setup(**config)

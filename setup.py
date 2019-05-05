import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-pygments-renderer',
    version='0.0.1',
    packages=find_packages(),
    description='Provides functionality for syntax highlighting using Pygments.',
    long_description=README,
    author='Masashi Shibata',
    author_email='contact@c-bata.link',
    url='https://github.com/c-bata/django-pygments-renderer',
    license='MIT',
    install_requires=[
        'Django',
        'pygments',
    ]
)

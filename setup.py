from setuptools import setup

setup(
    name='postit',
    version='0.0.0',
    packages=['postit', 'postit.adapter.cmd'],
    url='',
    license='gpl-3.0',
    author='',
    author_email='',
    description='Hexagonal Architecture in Python using Flask and SqlAlchemy',
    install_requires=['Click'],
    entry_points={
        'console_scripts': [
            'postit=postit.adapter.cmd.cli:cli'
        ],
    },
)

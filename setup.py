from setuptools import setup

setup(
    name='OMEGA',
    version='1.0',
    description='Matrix Operations',
    packages=['Omega'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Fraction',
        'Jinja2',
        'pyodbc',
        'requests'
    ],
)

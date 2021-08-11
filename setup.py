from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='Commandline user management utility',
    long_description=readme,
    author='John Giles',
    author_email='johngiles12345@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'hr=hr.cli:main',
        ]
    }
)


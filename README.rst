hr
========
CLI for managing user accounts on a Linux server based on the contents of a .JSON file.
Preparing for Development
-------------------------
1. Ensure ''pip'' and ''pipenv'' are installed.
2. Clone repository: ''git clone git@github.com:jgiles/hr''
3.''cd'' into repository.
4. Fetch development dependencies ''make install''
5. Activate virtualenv: ''pipenv shell''
Usage
-----
Pass in a path to an inventory.json file.
Example:
::
    $ hr path/to/inventory.json
An alternative usage is to pass in an --export flag to export the current user accounts to a .JSON file:
::
    $ hr --export path/to/inventory.json
Running Tests
-------------
Run tests locally using ''make'' if virtualenv is active:
::
    $ make
If virtualenv isn’t active then use:
::
    $ pipenv run make


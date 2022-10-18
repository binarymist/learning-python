pyenv is like nvm but instead of for nodejs for python. Seems like asdf is a better option for all

Probably a better way to install python versions but I haven't done it yet:

* https://github.com/asdf-vm/asdf
* https://github.com/danhper/asdf-python
* https://asdf-vm.com/guide/getting-started.html#global talks about using the systems python via asdf, then links to: https://asdf-vm.com/manage/versions.html#fallback-to-system-version
* All asdf commands https://asdf-vm.com/manage/commands.html

Virtual Environments:

* pip is a package installer
* pipenv is a dependency manager, like npm for NodeJS, but it installs everything required to run a project into ~/.local/share/virtualenvs/
* virtualenv is used by pipenv, but can be used standalone. It does what pipenv does but installs in your current dir. Usually you'll install into a venv/ dir though
  * As of Python 3.3 there is a module called venv (https://docs.python.org/3/library/venv.html) which is run from python, this is now the preferred way to create virtual environments
  * There is now also virtualenvwrapper https://docs.python-guide.org/dev/virtualenvs/#virtualenvwrapper which sounds very similar to virtualenv but more polished
* pyenv is a tool to allow multiple versions of the Python interpreter to be installed at the same time. May as well just use asdf.
  
Installed pipenv https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv although may not need it with using `python3 -m venv`  
`pip install --user pipenv`
  
pipenv creates virtualenvs and installs project specific dependencies. Installs into ~/.local/share/virtualenvs/
  
Sounds like venv followed by pipenv are the best choices.

So we're going to use venv

* doc: https://docs.python.org/3/library/venv.html

Using `python3 -m venv ...` requires python3.8-venv. On Linux Mint 21 (Vanessa), python3-venv is already installed

* For Linux Mint 20.3: https://www.techcoil.com/blog/how-to-install-python3-venv-on-ubuntu-16-04/, For Linux Mint 21 just install python3-venv using Synaptic Package Manager
* The best usage guide is Effective Python (2nd Edition) - Item 83
* Create the virtual environment: python3 -m venv .venv
* Get into the virtual enviroment (activate it): source .venv/bin/activate
* Install dependencies:  
  The following will generate an error because there is no requests installed into our virtual environment yet.  
  `python3 -c 'import requests'`  
  Using `python3 -m pip` ensures that packages are installed for the correct version of Python.  
  `python3 -m pip install requests`  
  The following should now not generate an error:  
  `python3 -c 'import requests'`
* Get out of the virtual environment (deactivate it): `deactivate`
* To remove a virtual environment, just delete the directory
  
## Reproducing Dependencies

To save all of my explicit package dependencies into a file, from within your virtual environment run the following command:  
`python3 -m pip freeze > requirements.txt`

To list the installed packagtes in the virtual environment run the following command:  
`python3 -m pip list`

To install packages from requirements.txt (still in a virtual environment) run the following command:  
`python3 -m pip install -r <path-to-requirements.txt>`

Moving a virtual environment breaks everying because all of the paths are hard-coded. This doesn't matter though. Just use:

* `python3 -m pip freeze ...` on the old one
* Create a new virtual environment somewhere else
* And reinstall everything from the requirements.txt file

The version of Python must be managed seperatly to the requirements.txt file.

When we need other versions of Python3 use asdf. [Using asdf python with virtual env](https://github.com/danhper/asdf-python/issues/47).


## Hydro.iO

### Requirements

Before starting, make sure you have the following installed:

* PostgreSQL
* python
* pip
* It's recommended to use a virtual environment for dependencies.  On Mac OS:
    * `sudo pip install virtualenv`
    * `sudo pip install virtualenvwrapper`
    * Finally, add the following to your `~/.bash_profile`:
        * `source /usr/local/bin/virtualenvwrapper.sh`

### Getting Started
As mentioned, it's recommended to use a virtual environment for the project dependencies.  This will prevent your local python installation from getting clouded with dependencies that might not jive with other projects.  It also makes it easy to mymic different deployment environments.  For example:

```bash
$ mkvirtualenv hydro-io
New python executable in hydro-io/bin/python
Installing setuptools, pip...done.
(hydro-io)$ 
```

Now, let's install our dependencies:
```bash
(hydro-io)$ sudo pip install -r requirements.txt
```
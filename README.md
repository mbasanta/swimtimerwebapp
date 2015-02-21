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

### Dependencies
As mentioned, it's recommended to use a virtual environment for the project dependencies.  This will prevent your local python installation from getting clouded with dependencies that might not jive with other projects.  It also makes it easy to mymic different deployment environments.  For example:

```bash
$ mkvirtualenv hydro-io
New python executable in hydro-io/bin/python
Installing setuptools, pip...done.
(hydro-io)$ 
```

You can disable the virtual environment by running `deactivate` and re-enable with `workon hydro-io`.

Lastly, install the dependencies dependencies:
```bash
(hydro-io)$ sudo pip install -r requirements.txt
```

### Database Setup
First, copy the template for local database settings:

```bash
(hydro-io)$ cd webapp/webapp/settings
(hydro-io)$ cp local.py.template local.py
```

Edit `local.py` to reflect the settings for a newly created database.

Finally, initialize the database using South from the __webapp__ directory:

```bash
(hydro-io)$ python manage.py syncdb
...
(hydro-io)$ python manage.py migrate base
...
(hydro-io)$ python manage.py migrate oauth2_provider
...
(hydro-io)$ python manage.py migrate swimapp
...
```

### Admin User Setup
TODO
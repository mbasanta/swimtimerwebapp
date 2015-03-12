# Hydro.iO

## Requirements

Before starting, make sure you have the following installed:

* PostgreSQL
* [Redis](#redis)
* python
* pip
* It's recommended to use a virtual environment for dependencies.  On Mac OS:
    * `sudo pip install virtualenv`
    * `sudo pip install virtualenvwrapper`
    * Finally, add the following to your `~/.bash_profile`:
        * `source /usr/local/bin/virtualenvwrapper.sh`

## Dependencies
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

## Database Setup
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

## Redis/Celery

When running the application locally you'll need to have Redis and Celery
running. These are used for background tasks such as file upload processing,
messageing and sending emails.

### <a name="redis"></a>Redis

Redis is easy to install and maintain with [HomeBrew](http://brew.sh)

```bash
$ brew install redis
```

Redis is easy enough to run, just execute `redis-server` from the command line
and the server will start. If you want to check out redis while it's running,
`redis-cli` opens the Redis command line client.

### Celery

Celery should have been installed when the pip dependencies where installed.
Celery is slightly more complex to run.

* Go to the project directory, the same directory that contains `manage.py`
* Ensure you activate your virtual enviroment if necessary
* Execute `celery -A webapp worker --loglevel=info`
    * `-A webapp` identifies the app use with celery
    * `worker` creates a worker instance of celery
    * `--loglevel=info` logs everything, you can change this if it's too much


## Admin User Setup
TODO

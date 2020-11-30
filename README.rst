|CircleCI|
|GitHub|
|Coverage|
|License|

.. |PyPI|

AIOHTTP Application Template
============================

This template repository is meant to serve as a starting point for anyone wanting to build an ``aiohttp``-based
web application and run that web application on Heroku (or a similar service).  It provides basic structure and
setup for a web application using a MongoDB database with Python ``motor``, and the base code is set up with
``pytest`` unit testing and continuous integration with CircleCI (and GitHub Actions).

How to use this template
------------------------

You should just be able to create your own repository based on this template by just choosing this template
during the new repository creation form on GitHub, or by clicking the "Use this template" button on this template's
GitHub main page.  (I highly recommend that you select the *"Include all branches"* radio button, which will give
you an "ready-to-go" GitHub Pages branch (``gh-pages``) for your application's documentation.  If you don't do this,
and you want to enable GitHub Pages for your new repository, you will have to manually add a ``.nojekyll`` file to
the ``gh-pages`` branch.)

After creating a new repository based on this template, you will probably want to customize your version for
your purposes.  Some things you should consider to customize this template for your application include:

- Change the main Python package name to the name of your app by changing the name of the ``myapp`` directory
- Update the ``Procfile`` to use this new package name
- Update the ``setup.py`` file to meet your needs (i.e., short and long descriptions, etc.)
- Update the ``README.rst`` file as you see fit
- Change the LICENSE, if you so choose
- Update the documentation in the ``docs/`` folder
- Change the name of the conda environment in the ``.circleci/environment.yml`` file (entirely optional!)


Some notes on the design
------------------------

aiohttp
~~~~~~~

This application is build using ``aiohttp``, an asynchronous web server/client
framework for Python 3.5+.  If you are unfamiliar with asynchronous programming in
Python (namely, Python 3.5+'s ``asyncio``), then you should read up on it here:

- https://docs.python.org/3/library/asyncio.html
- https://realpython.com/async-io-python/

The ``aiohttp`` package provides a web server and client that uses this fundamental
``asyncio`` functionality.  To learn more about ``aiohttp``, you can read up on it here:

- https://docs.aiohttp.org/en/v3.0.1/tutorial.html#aiohttp-tutorial

There are many alternatives to ``aiohttp``, including the more "sophisticated" Django
and Flask frameworks, but I chose ``aiohttp`` here because this "app" is designed to
be very simple.  If you were to grow this app into something that needed much more
functionality, was more widely used, and needed greater security, I would definitely
go to Django or Flask and scale your app behind a reverse proxy server like Nginx.
However, for these purposes (i.e., think "small, private GitHub App"), this should
work quite well.  And this serves as an introduction to the concepts that you would
then expand upon if you moved to Django or Flask in the future.


Heroku
~~~~~~

This app is also designed to run on Heroku.  It is not large or demanding, so we
do not need to pay for anything, yet.  The launch command that is needed for the
app to run on Heroku is stored in the ``Procfile`` file, and the version of Python
needed to run is specified in the ``runtime.txt`` file.  That is all you need to
set this app up to run on Heroku.  This is enough to tell Heroku to "build" your
app with the Python build-pack.

Heroku is not perfect.  As I already mentioned, this app is designed to be very
light-weight; it is not meant for a heavily-used production service.  If you need
to grow this app into something larger, then you might need to pay for additional
capabilities on Heroku.  If that day comes, you may find that Heroku is too expensive.
However, Heroku's free Platform-as-a-Service model is incredibly easy to use and
configure, and for something small like this, it is perfect.


motor
~~~~~

While Heroku provides a free-level MongoDB service as a "plug-in" for your Heroku
app, MongoDB.com also provides a free-tier database of the same size.  Using
MongoDB.com means that you only need to configure the app and your databose on
MongoDB.com directly (with the dashboard).  However, using Heroku's plugin means
you need to configure the app, the MongoDB database itself, and the plugin via
the Heroku dashboard.  I find that needlessly complicated for something this
simple.  So, I just designed this app to use MongoDB.com directly.  Heroku need
know nothing about it.

MongoDB.com provides a cloud-based DBaaS which has a free "sandbox" level (512 MB).
The app does not need much storage, so we use this service for free, but we may
need to upgrade to a paid service in the future, or switch to a different DB
solution.

The recommended ``asyncio``-compatible driver for MongoDB is ``motor``.  The tutorial
for ``motor`` with ``asyncio`` can be found here:

- https://motor.readthedocs.io/en/stable/tutorial-asyncio.html


CircleCI
~~~~~~~~

This app also has continuous integration enabled with CircleCI.  This means that
Heroku can be used to autodeploy when CI tests pass.


Installation
------------

This application can be installed with ``pip`` or directly with ``setup.py``:

.. code-block:: bash

   $ python setup.py install

or

.. code-block:: bash

   $ pip install .


Running Locally
---------------

To run this application locally, you need simply run:

.. code-block:: bash

   $ python -m myapp

However, this application uses ``click`` for its CLI, which means you can get the
full help description with:

.. code-block:: bash

   $ python -m myapp --help
   Usage: myapp [OPTIONS]

   Options:
     --version          Show the version and exit.
     --host TEXT        Server IP address
     --port INTEGER     Server port number
     --logging INTEGER  Logging output level
     --mongouri TEXT    MongoDB URI
     --mongodb TEXT     MongoDB Database Name
     --config PATH      User-defined configuration file location
     --help             Show this message and exit.


.. |CircleCI| image:: https://badgen.net/circleci/github/ncar-xdev/aiohttp_app_template/master
    :target: https://circleci.com/gh/ncar-xdev/aiohttp_app_template
    :alt: Tests

.. |GitHub| image:: https://badgen.net/github/checks/ncar-xdev/aiohttp_app_template/master
    :target: https://github.com/ncar-xdev/aiohttp_app_template/actions
    :alt: GitHub

.. |Coverage| image:: https://badgen.net/codecov/c/github/ncar-xdev/aiohttp_app_template
    :target: https://codecov.io/gh/ncar-xdev/aiohttp_app_template
    :alt: Coverage

.. |License| image:: https://badgen.net/github/license/ncar-xdev/aiohttp_app_template
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: License

.. |PyPI| image:: https://badgen.net/pypi/v/aiohttp_app_template?label=pypi
    :target: https://pypi.org/project/aiohttp_app_template
    :alt: PyPI

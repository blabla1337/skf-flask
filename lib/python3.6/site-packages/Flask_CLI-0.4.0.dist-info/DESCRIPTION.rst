===========
 Flask-CLI
===========

About
=====

Flask-CLI is a backport of Flask 1.0 new click integration to Flask 0.10. Do not install this package if you use Flask 1.0+.

Installation
============

Flask-CLI is on PyPI so all you need is: ::

    pip install flask-cli


Usage
=====

Initialize the extension like this:

.. code-block:: python

   from flask import Flask
   from flask_cli import FlaskCLI
   app = Flask('myapp')
   FlaskCLI(app)

   @app.cli.command()
   def mycmd():
       click.echo("Test")

   @app.shell_context_processor
   def myctx():
       return {'myvar': 'value'}

Import from this library instead of ``flask.cli``:

.. code-block:: python

   from flask_cli import FlaskGroup

Documentation
=============

Documentation is readable at http://flask-cli.readthedocs.org or can be
build using Sphinx: ::

    pip install Sphinx
    python setup.py build_sphinx

Testing
=======

Running the test suite is as simple as: ::

    python setup.py test



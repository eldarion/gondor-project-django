================
Django on Gondor
================

This Django project is a very simple example that will work out-of-the-box on
Gondor. You can use this to start your project that will be hosted on Gondor.

Usage
=====

Create a virtual environment (see `virtualenv`_) and install Django::

    pip install Django==1.4.2

Now you are ready to start your Django project. Use ``startproject`` to get
this template.

::

    django-admin.py startproject --template=https://gondor.io/p/django/ --extension=py,yml <project_name>
    cd <project_name>

To make this project runnable you will need to install its dependencies in
your virtual environment.

::

    pip install -r requirements.txt

You are now ready to deploy this project to Gondor!

If you use git::

    git init
    git add .
    git commit -m "Initial project layout"
    gondor deploy primary master

If you use mercurial::

    hg init
    hg add .
    hg commit -m "Initial project layout"
    gondor deploy primary default

.. _virtualenv: http://www.virtualenv.org/

Layout
======

The project layout follows the Django 1.4+ layout.

::

    gondor-project-django/
        .git or .hg (version control metadata)
        fixtures/
            initial_data.json (where any data that should be loaded into the database on each deploy)
        gondor.yml (Gondor configuration file)
        manage.py
        project_name/ (project's Python package)
            __init__.py
            settings.py
            settings_gondor.py (Django settings for use on Gondor)
            static/ (see README in directory)
            templates/ (where templates for your project goes)
            urls.py
            wsgi.py (WSGI entry point for Django)
        requirements.txt (pip file to declare dependencies)

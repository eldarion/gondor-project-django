================
Django on Gondor
================

This Django project is a very simple example that will work out-of-the-box on
Gondor. You can use this to start your project that will be hosted on Gondor.

Usage
=====

Use the files here to start your own project. To make this project runnable
you will need to install its dependencies in your environment (ideally you
create a virtual environment with `virtualenv`_.)

::

    pip install -r requirements.txt

Now, you will likely want to customize the naming to better match your
actual project.

``project_name`` is the Python package. You will want to rename this and
every where ``project_name`` appears in the code base. This includes:

 * ``manage.py`` and ``wsgi.py`` when setting ``DJANGO_SETTINGS_MODULE``
   in ``setdefault``
 * ``settings.py`` when setting ``ROOT_URLCONF`` and ``WSGI_APPLICATION``
 * ``gondor.yml`` for ``wsgi.entry_point`` and ``env.DJANGO_SETTINGS_MODULE``

When you initialize your version control system be sure to do this in the
directory containing ``project_name`` (the Python package.)

You are now ready to deploy this project to Gondor!

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

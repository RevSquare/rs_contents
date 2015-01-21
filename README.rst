###############
Contents
###############

Base app for content models delivered by RevSquare. Tested with django 1.7.x

* Provide base models with content in `rs_contents.models`

* Provide mix view with preview in `rs_contents.views`

* Provide preview view mix and admin model in `rs_contents.preview`




*******
Install
*******

It is strongly recommanded to install this theme from GIT with
 PIP onto you project virtualenv.

.. code-block::  shell-session

    pip install git+ssh://git@revsquare-test.com/rs-contents.git


*****
Setup
*****


.. code-block::  python

    INSTALLED_APPS = (
        ...
        'rs_contents'
        ...
    )


*****
Tests
*****


.. code-block::  shell-session
    python manage.py test cms_base


*******************
Additional Packages
*******************
git.revsquare.com/revsquare/economist-content-page.git@0.2.7.3




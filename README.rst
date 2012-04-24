========================
Plone catalog regression
========================

A buildout for finding out in which version of Plone did we have a catalog
regression.


How to use
----------

This repo contains buildouts for several Plone versions:

* ``plone4.0.cfg``
* ``plone4.1.cfg``
* ``plone4.2.cfg``

Choose one version and build your environment::

  $ python2.6 bootstrap.py
  $ bin/buildout -c plone4.1.cfg

Now you can run the test to see if catalog results are as they should be or
not::

  $ bin/test -s catalog.regression
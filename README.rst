========================
Plone catalog regression
========================

A buildout for finding out in which version of Plone we introduced a catalog
regression.


How to use
----------

This repo contains buildouts for several Plone versions:

* ``plone4.0.9.cfg``
* ``plone4.1.4.cfg``
* ``plone4.2b2.cfg``

Choose one version and build your environment::

    $ python2.6 bootstrap.py
    $ bin/buildout -c plone4.1.4.cfg

Now you can run the test to see if catalog results are as they should be or
not::

    $ bin/test -s catalog.regression

You can also import test articles into your Plone site and test manually
(assuming your Plone instance has an id of ``Plone``)::

    $ bin/instance debug
    from collective.transmogrifier.transmogrifier import Transmogrifier
    transmogrifier = Transmogrifier(app.Plone)
    transmogrifier('Import 100 articles')
    app.Plone.portal_catalog.clearFindAndRebuild()
    import transaction; transaction.commit()


.. _alternations:

Alternating results problem
---------------------------

The problem is that in newer Plone releases, querying the catalog with the same
query parameters multiple times returns two different sets of results.

To reproduce, first run tests on Plone 4.0.9, then on 4.1.4. You will see
that in 4.1.4 the top result for the first and second query are different
(although query parameters are identical)::

    $ git clone git://github.com/zupo/catalog.regression.git
    $ cd catalog.regression
    $ python2.6 bootstrap.py -c plone4.0.9.cfg

    $ bin/buildout -c plone4.0.9.cfg
    $ bin/test -s catalog.regression
    [... snip ...]
    Ran 3 tests with 0 failures and 0 errors in 11.995 seconds.

    $ bin/buildout -c plone4.1.4.cfg
    $ bin/test -s catalog.regression
    [... snip ...]
    FAIL: first and second query returned a different top result: 'what-is-the-green-bean-dog-diet.txt' vs. 'a-guide-to-candy-vending-machines.txt '


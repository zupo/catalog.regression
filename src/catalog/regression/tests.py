# -*- coding: utf-8 -*-
"""Module where all TestCases live."""

from collective.transmogrifier.transmogrifier import Transmogrifier
from plone.app.testing import IntegrationTesting
from plone.app.testing import login
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from Products.CMFCore.utils import getToolByName

import transaction
import unittest2 as unittest

QUERY = {
    'b_size': 10,
    'portal_type': ['News Item', 'Image', 'Topic', 'Link', 'File', 'Folder', 'Document', 'Event'],
    'SearchableText': 'dog',
    'show_inactive': False,
    'b_start': 0,
    'path': '/plone'
}


class CatalogRegressionLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import catalog.regression
        self.loadZCML(package=catalog.regression)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        #applyProfile(portal, 'niteoweb.plr:default')

        # Login as Manager
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)


FIXTURE = CatalogRegressionLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="CatalogRegressionLayer:Integration")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class Test3Articles(IntegrationTestCase):
    """Test search results alternation for 3 articles."""

    def test_search_alternation(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.catalog = getToolByName(self.portal, 'portal_catalog')

        # Create test content by importing test articles with Transmogrifier
        transmogrifier = Transmogrifier(self.portal)
        transmogrifier('Import 3 articles')

        # Commit all changes
        self.portal.portal_catalog.clearFindAndRebuild()
        transaction.commit()

        # query catalog twice
        first = self.catalog(QUERY)[:3]
        second = self.catalog(QUERY)[:3]

        self.assertEquals(first[0].id, second[0].id,
            "FAIL: first and second query returned a differnet top result: '%s' vs. '%s '"
                % (first[0].id, second[0].id))


class Test10Articles(IntegrationTestCase):
    """Test search results alternation for 10 articles."""

    def test_search_alternation(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.catalog = getToolByName(self.portal, 'portal_catalog')

        # Create test content by importing test articles with Transmogrifier
        transmogrifier = Transmogrifier(self.portal)
        transmogrifier('Import 10 articles')

        # Commit all changes
        self.portal.portal_catalog.clearFindAndRebuild()
        transaction.commit()

        # query catalog twice
        first = self.catalog(QUERY)[:3]
        second = self.catalog(QUERY)[:3]

        self.assertEquals(first[0].id, second[0].id,
            "FAIL: first and second query returned a differnet top result: '%s' vs. '%s '"
                % (first[0].id, second[0].id))


class Test100Articles(IntegrationTestCase):
    """Test search results alternation for 100 articles."""

    def test_search_alternation(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.catalog = getToolByName(self.portal, 'portal_catalog')

        # Create test content by importing test articles with Transmogrifier
        transmogrifier = Transmogrifier(self.portal)
        transmogrifier('Import 100 articles')

        # Commit all changes
        self.portal.portal_catalog.clearFindAndRebuild()
        transaction.commit()

        # query catalog twice
        first = self.catalog(QUERY)[:3]
        second = self.catalog(QUERY)[:3]

        self.assertEquals(first[0].id, second[0].id,
            "FAIL: first and second query returned a differnet top result: '%s' vs. '%s '"
                % (first[0].id, second[0].id))

# -*- coding: utf-8 -*-
"""Module where all TestCases live."""

from plone.app.testing import IntegrationTesting
from plone.app.testing import login
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from Products.CMFCore.utils import getToolByName

import unittest2 as unittest


class CatalogRegressionLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import catalog.regression
        self.loadZCML(package=catalog.regression)
        #TODO: z2.installProduct(app, 'catalog.regression')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        #applyProfile(portal, 'niteoweb.plr:default')

        # Login as Manager
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)

        # Create test content by importing test articles with Transmogrifier
        from collective.transmogrifier.transmogrifier import Transmogrifier
        transmogrifier = Transmogrifier(portal)
        transmogrifier('Test data import')

        # Commit all changes
        portal.portal_catalog.clearFindAndRebuild()
        import transaction
        transaction.commit()

    def tearDownZope(self, app):
        """Tear down Zope."""
        #TODO: z2.uninstallProduct(app, 'catalog.regression')
        pass


FIXTURE = CatalogRegressionLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="CatalogRegressionLayer:Integration")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class TestSearchResultsOrdering(IntegrationTestCase):
    """Test the order of search results."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.catalog = getToolByName(self.portal, 'portal_catalog')

    def test_search_results_order(self):
        """Test the order of search results."""
        results = self.catalog(SearchableText='dog')

        import pdb; pdb.set_trace( )
        self.assertEquals(results[0].id, 'foo id')

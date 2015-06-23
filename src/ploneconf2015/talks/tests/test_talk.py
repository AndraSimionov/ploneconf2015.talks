# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from ploneconf2015.talks.testing import PLONECONF2015_TALKS_INTEGRATION_TESTING  # noqa
from ploneconf2015.talks.interfaces import ITalk

import unittest2 as unittest


class TalkIntegrationTest(unittest.TestCase):

    layer = PLONECONF2015_TALKS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Talk')
        schema = fti.lookupSchema()
        self.assertEqual(ITalk, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Talk')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Talk')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ITalk.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Talk', 'Talk')
        self.assertTrue(
            ITalk.providedBy(self.portal['Talk'])
        )

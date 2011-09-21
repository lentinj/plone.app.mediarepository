from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig
from plone.app.testing.layers import IntegrationTesting
from plone.app.testing.layers import FunctionalTesting

from plone.dexterity.utils import createContent

class PAMediaRepository(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # load ZCML
        import plone.app.mediarepository
        xmlconfig.file('configure.zcml', plone.app.mediarepository, context=configurationContext)
    
    def setUpPloneSite(self, portal):
        # install into the Plone site
        applyProfile(portal, 'plone.app.mediarepository:default')
        
        # add a manager user
        portal['acl_users'].userFolderAddUser('admin',
                                              'secret',
                                              ['Manager'],
                                              [])

MEDIAREPOSITORY_FIXTURE = PAMediaRepository()
MEDIAREPOSITORY_INTEGRATION_TESTING = IntegrationTesting(bases=(MEDIAREPOSITORY_FIXTURE,), name="PAMediaRepository:Integration")
MEDIAREPOSITORY_FUNCTIONAL_TESTING = FunctionalTesting(bases=(MEDIAREPOSITORY_FIXTURE,), name="PAMediaRepository:Functional")

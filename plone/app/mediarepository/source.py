from plone.formwidget.contenttree import UUIDSourceBinder

from zope.app.component.hooks import getSite

class MediaRepoSourceBinder(UUIDSourceBinder):
    def __init__(self):
        # Ideally would set navigation tree query at this point, but don't seem
        # to be able to get a site. Wait until call
        super(MediaRepoSourceBinder, self).__init__()

    def __call__(self, context):
        site = getSite()
        repo = site.restrictedTraverse('media-repository')
        repoPath = '/'.join(repo.getPhysicalPath())
        self.navigation_tree_query = {'path': {'query': repoPath}}
        source = super(MediaRepoSourceBinder, self).__call__(context)
        return source

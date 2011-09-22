from Products.Five import BrowserView
from zope.component import getUtility
from zope.app.intid.interfaces import IIntIds


class Picker(BrowserView):
    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)

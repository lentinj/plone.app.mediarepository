from Products.Five import BrowserView


class Picker(BrowserView):
    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)

class AbstractHandler:
    def handle(self, request):
        self._next.handle(request)
        
    def set_next(self, handler):
        self._next = handler

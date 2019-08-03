class AbstractHandler:
    def handle(self, request):
        try:
            print(self._next)
            self._next.handle(request)
            print(request)
        except AttributeError:
            pass
        
    def set_next(self, handler):
        self._next = handler

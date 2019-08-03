class AbstractHandler:
    def handle(self, request):
<<<<<<< HEAD
	try:
            request._next.handle(request)
=======
        try:
            self._next.handle(request)
>>>>>>> dd67d387298f16826eb6dabd04c93104db8b0dc0
        except AttributeError:
            pass
        
    def set_next(self, handler):
        self._next = handler

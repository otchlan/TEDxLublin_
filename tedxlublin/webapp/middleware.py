from django.http import HttpResponseRedirect

class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/pl/') and request.path != '/pl':
            return HttpResponseRedirect('/pl' + request.path)
        return self.get_response(request)

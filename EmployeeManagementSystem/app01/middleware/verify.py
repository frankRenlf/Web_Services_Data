from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class Authorise(MiddlewareMixin):
    def process_request(self, request):
        return
        # if request.path_info in ["/login", "/image/code"]:
        #     return
        # if not request.session.get("info"):
        #     return redirect('/login')

    def process_response(self, request, response):
        return response

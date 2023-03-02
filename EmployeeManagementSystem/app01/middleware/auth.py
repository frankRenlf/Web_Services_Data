from django.utils.deprecation import MiddlewareMixin


class M1(MiddlewareMixin):
    def process_request(self, request):
        print("m1 in")

    def process_response(self, request, response):
        print("m2 out")
        return response

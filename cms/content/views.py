from django.http import HttpResponse, HttpRequest

def hello_world(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")
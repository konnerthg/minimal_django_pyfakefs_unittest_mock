from django.http import HttpResponse


def foo():
    pass


def index(request):
    foo()
    return HttpResponse("Hello World")

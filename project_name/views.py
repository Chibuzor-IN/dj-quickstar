from django.http import HttpResponse

def index(request, *args, **kwargs):
    return HttpResponse('Hello world')
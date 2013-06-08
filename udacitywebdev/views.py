from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name = "front")
def hello_udacity(request):
    return Response("Hello, Udacity!")

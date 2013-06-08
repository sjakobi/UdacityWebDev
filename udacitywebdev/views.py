from pyramid.view import view_config

@view_config(route_name = "front", renderer="templates/simple-front.jinja2")
def hello_udacity(request):
    return dict(title="Hello, Udacity!")

from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route("front", "/")
    config.scan()
    return config.make_wsgi_app()

# https://www.howtoing.com/how-to-deploy-python-wsgi-applications-using-a-cherrypy-web-server-behind-nginx/
# Import your application as:
# from wsgi import application
# Example:

from stock.wsgi import application
from stock import settings
# Import CherryPy
import cherrypy

if __name__ == '__main__':

    config = {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': settings.STATIC_ROOT,
        'tools.expires.on': True,
        'tools.expires.secs': 86400
    }
    cherrypy.tree.mount(None, settings.STATIC_URL, {'/': config})

    print cherrypy.config.values()
    # Mount the application
    cherrypy.tree.graft(application, "/")

    # Unsubscribe the default server
    cherrypy.server.unsubscribe()

    # Instantiate a new server object
    server = cherrypy._cpserver.Server()

    # Configure the server object
    server.socket_host = "0.0.0.0"
    server.socket_port = 8080
    server.thread_pool = 30

    # For SSL Support
    # server.ssl_module            = 'pyopenssl'
    # server.ssl_certificate       = 'ssl/certificate.crt'
    # server.ssl_private_key       = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt'

    # Subscribe this server
    server.subscribe()

    # Example for a 2nd server (same steps as above):
    # Remember to use a different port

    # server2             = cherrypy._cpserver.Server()

    # server2.socket_host = "0.0.0.0"
    # server2.socket_port = 8081
    # server2.thread_pool = 30
    # server2.subscribe()

    # Start the server engine (Option 1 *and* 2)

    cherrypy.engine.start()
    cherrypy.engine.block()
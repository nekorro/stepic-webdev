from wsgiref.simple_server import make_server
import urlparse

def wsgi_stepic19_app(environ, start_response):
   qs = environ['QUERY_STRING']
   output = qs.replace('&','\n')
   start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(output)))
        ])
   return iter([output])

httpd = make_server('', 8000, wsgi_stepic19_app)
print "Serving HTTP on port 8000..."

# Respond to requests until process is killed
httpd.handle_request()

from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults
from urllib.parse import parse_qs


def simple_app(environ, start_response):
    #    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    qs = environ.get('QUERY_STRING')
    ret = [("%s=%s\n" % (key, value[0])).encode("utf-8")
           for key, value in parse_qs(qs).items()]
    return ret

httpd = make_server('', 8000, simple_app)
print("Serving HTTP on port 8000...")

# Respond to requests until process is killed
httpd.handle_request()

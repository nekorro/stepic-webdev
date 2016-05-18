def wsgi_stepic19_app(environ, start_response):
    qs = environ['QUERY_STRING']
    output = qs.replace('&', '\n')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(output)))
    ])
    return iter([output])

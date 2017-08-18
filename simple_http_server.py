#!/usr/bin/env python

try:
    # python 3
    from http.server import SimpleHTTPRequestHandler
    import socketserver
except ImportError:
    # python 2
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    import SocketServer as socketserver


ADDR = "127.0.0.1"
PORT = 8000


class RequestHandler(SimpleHTTPRequestHandler):
    """
    Add path info in error message
    e.g.: 404 - File not found
    """
    def send_error(self, code, message=None):
        path_info = repr(self.path)
        if message is None:
            message = path_info
        else:
            message += " - %s" % path_info
        super(RequestHandler, self).send_error(code, message)


httpd = socketserver.TCPServer(
    (ADDR, PORT), RequestHandler
)

print("serving at http://%s:%s" % (ADDR, PORT))
httpd.serve_forever()


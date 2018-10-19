import logging

import http.server
import socketserver

LOGGER = logging.getLogger(__name__)

class Server(object):

    class ServerHandler(http.server.SimpleHTTPRequestHandler):

        def do_POST(self):
            content_len = int(self.headers.get('content-length', 0))
            post_body = self.rfile.read(content_len)
            self.post_callback(post_body)

    def listen(self, host, port, processor):
        handler = self.ServerHandler
        handler.post_callback = processor

        httpd = socketserver.TCPServer((host, port), handler)

        LOGGER.info("Listening on %s:%s", host, port)
        httpd.serve_forever()
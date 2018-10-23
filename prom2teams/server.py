import logging

import http.server

LOGGER = logging.getLogger(__name__)

class Server(object):

    class ServerHandler(http.server.SimpleHTTPRequestHandler):

        def do_POST(self):
            # Send the response
            self.send_response(200)
            self.end_headers()
            # Process the content
            try:
                content_len = int(self.headers.get('content-length', 0))
                self.post_callback(self.rfile.read(content_len))
            except Exception as e:
                LOGGER.error("Failed to process request: %s", e)

    def listen(self, host, port, processor):
        handler = self.ServerHandler
        handler.post_callback = processor

        httpd = http.server.HTTPServer((host, port), handler)
        httpd.protocol_version = 'HTTP/1.1'

        LOGGER.info("Listening on %s:%s", host, port)
        httpd.serve_forever()
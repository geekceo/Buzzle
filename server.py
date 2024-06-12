from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from tools import parser
import urls

import sys

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parser.Parser(html='test.html').parse()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        #self.wfile.write(bytes(open(file='output.html', mode='r').read(), encoding='UTF-8'))

        for path in urls.urlpathes:

            if path.path == self.path:

                path.controller(self)

        

        

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, ip='127.0.0.1', port=8000):

    server_address = (ip, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting Buzzle on port {port}")

    def __restart():

        print('A')

        httpd.shutdown()
        httpd.serve_forever()

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:

        print('\nBye!')
        httpd.shutdown()

    except Exception as error:

        raise repr(error)

if __name__ == '__main__':

    ip, port = (data for data in sys.argv[1].split(':'))

    run(ip=ip, port=int(port))
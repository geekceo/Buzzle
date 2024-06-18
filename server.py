from http.server import BaseHTTPRequestHandler, HTTPServer
from tools import parser, webserver, linker
import urls
import json
import config

import sys

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #parser.Parser(html='test.html').parse()
        linker.Linker.Storage.init_templates(templates=config.TEMPLATES)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        #self.wfile.write(bytes(open(file='output.html', mode='r').read(), encoding='UTF-8'))

        '''Loop for all urls from custom urls.py file'''
        for path in urls.urlpathes:

            if path.path in self.path:

                '''Send first request as argument to parse base data'''
                request: webserver.Request = webserver.Request(b_request=self.__dict__)

                path.controller(request)

    def do_POST(self):

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        for path in urls.urlpathes:

            if path.path in self.path:

                '''Send first request as argument to parse base data'''
                request: webserver.Request = webserver.Request(b_request=self.__dict__)

                path.controller(request)


        

        

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, ip='127.0.0.1', port=8000):

    server_address = (ip, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting Buzzle on port {port}")

    def __restart():

        print('A')

        httpd.shutdown()
        httpd.serve_forever()

    linker.Linker.Storage.init_templates(templates=config.TEMPLATES)

    #print(linker.Linker.Storage.get_template_content('base.html'))

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
from http.server import BaseHTTPRequestHandler


class Request:

    def __get_query(self, path: str) -> dict:
        
        if '?' in path:

            queryset = path.split('?')[1]
            query_vars = queryset.split('&')
            query_dict = {data.split('=')[0]: data.split('=')[1] for data in query_vars }

            return query_dict

        return False


    def __init__(self, b_request: dict[BaseHTTPRequestHandler] = None):

        for key, value in b_request.items():

            self.__setattr__(key, value)

        #print(self.__dict__)

        self.query_dict = self.__get_query(path=self.path)

        self.GET = self.query_dict if self.command == 'GET' and self.query_dict else True if self.command == 'GET' else False

        self.POST = self.query_dict if self.command == 'POST' and self.query_dict else True if self.command == 'POST' else False

        #print(self.GET)
        #print(self.POST)

        #print(b_request)

class Path:

    def __init__(self, path: str, controller: any, name: str):

        self.path = path
        self.controller = controller
        self.name = name
from tools import webserver
import os


class Linker:

    class Storage:

        @staticmethod
        def get_var(template_name: str, key: any):

            var: str | None = os.environ.get(key=f'{template_name}_{key}')

            if var != None:

                return var

            return False

        @staticmethod
        def set_var(template_name: str, key: any, value: any):

            os.environ[f'{template_name}_{key}'] = value

        

    class DOM:

        def render(request: webserver.Request, template_name: str, context: dict = None) -> None:

            if context != None:

                for key, value in context.items():

                    Linker.Storage.set_var(template_name=template_name, key=key, value=value)

            request.wfile.write(bytes(open(file='output.html', mode='r').read(), encoding='UTF-8'))
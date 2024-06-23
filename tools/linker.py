from tools import webserver, parser
import os


class Linker:

    class Storage:

        __template_storage: dict = {}

        def __new__(cls): ...

        @staticmethod
        def __type_conversion(var_value: str):

            if '\"' in var_value:

                return var_value.replace('\"', '')
            
            else:

                return var_value

        ''' Conversion for refactor variable value to original type (without quotes and e.t.c.) '''
        @staticmethod
        def get_var(template_name: str, key: any, conversion: bool = True):

            var_value: str | None = os.environ.get(key=f'{template_name.replace(".", "_")}_{key}')

            if var_value != None:

                return Linker.Storage.__type_conversion(var_value=var_value) if conversion else var_value

            return False

        @staticmethod
        def set_var(template_name: str, key: any, value: any):

            os.environ[f'{template_name.replace(".", "_")}_{key}'] = value

        @classmethod
        def init_templates(cls, templates: list) -> None:

            for template in templates:

                #print(template)

                cls.__template_storage[template] = []


        @classmethod
        def clear_template(cls, template: str) -> None:

            cls.__template_storage[template] = []


        @classmethod
        def write_template(cls, template: str, stroke: str) -> None:

            #print(stroke)

            cls.__template_storage[template].append(stroke)

        @classmethod
        def get_template_content(cls, template: str) -> str:

            return '\n'.join(cls.__template_storage[template])
        
        

        

    class DOM:

        def render(request: webserver.Request = None, template_name: str = 'buzzle_error', context: dict = None) -> None:

            print(Linker.Storage.get_template_content(template=template_name))

            if context != None:

                for key, value in context.items():

                    Linker.Storage.set_var(template_name=template_name, key=key, value=value)

            #request.wfile.write(bytes(open(file='output.html', mode='r').read(), encoding='UTF-8'))

            if template_name != 'buzzle_error':

                parser.Parser(template_name=template_name).parse()

                request.wfile.write(bytes(
                    Linker.Storage.get_template_content(template=template_name),
                    encoding='UTF-8'
                ))

            else:

                request.wfile.write(bytes(
                    open(file=f'{os.path.dirname(p=__file__)}/../docs/error.html').read(),
                    encoding='UTF-8'
                ))
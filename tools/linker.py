import os


class Linker:

    class Storage:

        @staticmethod
        def set_var(key: any, value: any):

            os.environ[key] = value

        @staticmethod
        def get_var(key: any):

            return os.environ.get(key, default=None)
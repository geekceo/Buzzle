import json
from tools import parser, space

'''
    Lexer to find buzzle code blocks
'''
class Lexer:

    @classmethod
    def __find_lexems(cls):

        '''
        Loop for each stroke of code
        '''
        for stroke in cls.strokes:

            '''Look for Buzzle blocks'''
            if ('[$' in stroke) and ('$]' in stroke):

                stroke = stroke.strip() # remove space from right and left sides of code stroke

                print(stroke)

                prompt: str = stroke.replace('[$', '').replace('$]', '') # remove Buzzle markers

                prompt_units: list = prompt.split(' ') # divide stroke by words

                print(prompt_units)

                '''Look for correct lexems in founded block'''
                for lexem, desk in cls.lexems.items():

                    if lexem in prompt_units:

                        print(f'{lexem}: {desk}')

                        prompt_units.remove(lexem) # remove founded lexem from code stroke to get next stroke unit

                        if desk == 'DEBUG':

                            value: str = [unit for unit in prompt_units if unit != ''] # make value for debug space
                            print(value)

                        elif desk == 'LET':

                            value: str = (data for data in ''.join(prompt_units).replace(' ', '').split('=')) # get vars key and value

                        #sp: space.Space = space.Space(desk=desk, value=value)

                        parser.Parser.write(sp=space.Space(desk=desk, value=value))




    def __new__(cls, strokes: list):
        
        cls.strokes: list = strokes

        cls.lexems: dict = json.loads(open(file='lexems.json', mode='r', encoding='UTF-8').read())

        cls.__find_lexems()

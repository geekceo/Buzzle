import json
from tools import parser, space, linker
import re

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

                #print(stroke)

                prompt: str = stroke.replace('[$', '').replace('$]', '') # remove Buzzle markers

                prompt_units: list = prompt.split(' ') # divide stroke by words

                #print(prompt_units)

                '''Look for correct lexems in founded block'''
                for lexem, desk in cls.lexems.items():

                    if lexem in prompt_units:

                        #print(f'{lexem}: {desk}')

                        prompt_units.remove(lexem) # remove founded lexem from code stroke to get next stroke unit

                        if desk == 'DEBUG':

                            value: str = [unit for unit in prompt_units if unit != ''] # make value for debug space
                            #print(value)

                        elif desk == 'LET':

                            value: str = (data for data in ''.join(prompt_units).replace(' ', '').split('=')) # get vars key and value

                        #sp: space.Space = space.Space(desk=desk, value=value)

                        parser.Parser.write(sp=space.Space(desk=desk, value=value))

            elif ('[[' in stroke) and (']]' in stroke): #for variable using blocks

                stroke: str = stroke.strip() # remove space from right and left sides of code stroke
                #print(stroke)

                # find the variable units in block
                matches = re.findall(r'\[\[\s*\$\w{1,}\s*\]\]', stroke)

                # loop for all matches of units
                for match in matches:

                    '''Find the variable name'''
                    unit: str = re.search(r'\$\w{1,}', match)[0]

                    '''Remove variable marker from name'''
                    unit = unit.split('$')[1]

                    '''Get the variable value'''
                    var_value = linker.Linker.Storage.get_var(unit)

                    if var_value != None:

                        stroke = stroke.replace(match, var_value, 1)

                        #print(stroke)

                '''Create a parser with desk is match unit and value is new stroke with variable values instead variable buzzle blocks'''
                parser.Parser.write(sp=space.Space(desk=match, value=stroke))





    def __new__(cls, strokes: list):
        
        cls.strokes: list = strokes

        cls.lexems: dict = json.loads(open(file='lexems.json', mode='r', encoding='UTF-8').read())

        cls.__find_lexems()

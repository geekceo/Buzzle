import json
from tools import lexer, space

'''
    * Parser to divide html/css code to strokes
    * Write/Update output file with html/css blocks instead of buzzle blocks
'''
class Parser:

    def __init__(self, html: str):

        self.html = html


    def parse(self):

        strokes = open(file=self.html, mode='r', encoding='UTF-8').read().split('\n')

        with open(file='output.html', mode='w', encoding='UTF-8') as output:

            output.write('\n'.join(strokes))

        lexer.Lexer(strokes=strokes)

    @staticmethod
    def write(sp: space.Space):

        print('*** PARSER WRITE ***')

        strokes: list = open(file='output.html', mode='r', encoding='UTF-8').read().split('\n')

        lexems: dict = json.loads(open(file='lexems.json', mode='r', encoding='UTF-8').read())

        for stroke in strokes:

            if ('[$' in stroke) and ('$]' in stroke):

                handle_stroke = stroke.strip()

                prompt: str = handle_stroke.replace('[$', '').replace('$]', '')

                prompt_units: list = prompt.split(' ')

                space_units_count: int = len(stroke) - len(stroke.lstrip())

                for lexem, desk in lexems.items():

                    if lexem in prompt_units:

                        if desk == sp.desk:

                            #print(f'{sp.desk}: {sp.value}')

                            strokes[strokes.index(stroke)] = ' ' * space_units_count + sp.get_space()
                            #print(' ' * space_units_count + sp.get_space())

                break

            elif ('[[' in stroke) and (']]' in stroke):

                space_units_count: int = len(stroke) - len(stroke.lstrip())

                strokes[strokes.index(stroke)] = ' ' * space_units_count + sp.get_space()

        with open(file='output.html', mode='w', encoding='UTF-8') as output:

            output.write('\n'.join(strokes))

        print('********************')

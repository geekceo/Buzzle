import json
from tools import lexer, space, linker
import config

'''
    * Parser to divide html/css code to strokes
    * Write/Update output file with html/css blocks instead of buzzle blocks
'''
class Parser:

    def __init__(self, html: str):

        self.html = html


    def parse(self):

        strokes = open(file=f'{config.BASE_DIR}/templates/{self.html}', mode='r', encoding='UTF-8').read().split('\n')

        with open(file='output.html', mode='w', encoding='UTF-8') as output:

            output.write('\n'.join(strokes))

        lexer.Lexer(strokes=strokes)

    @staticmethod
    def write(html_record: str | space.Space = None):

        #print(isinstance(html_record, space.Space))

        #record: str = html_record.get_space() if isinstance(html_record, space.Space) else html_record

        with open(file='output.html', mode='w', encoding='UTF-8') as output:

            #output.write(f'{record}\n')

            output.write(linker.Linker.Storage.get_template_content(template='base.html'))

            

        #print('*** PARSER WRITE ***')

        #strokes: list = open(file='output.html', mode='r', encoding='UTF-8').read().split('\n')
#
        #lexems: dict = json.loads(open(file='lexems.json', mode='r', encoding='UTF-8').read())
#
        #for stroke in strokes:
#
        #    if ('[$' in stroke) and ('$]' in stroke):
#
        #        handle_stroke = stroke.strip()
#
        #        '''remove func block markers'''
        #        prompt: str = handle_stroke.replace('[$', '').replace('$]', '')
#
        #        '''divide block content for any units'''
        #        prompt_units: list = prompt.split(' ')
#
        #        '''calculate spaces from start of stroke'''
        #        space_units_count: int = len(stroke) - len(stroke.lstrip())
#
        #        for lexem, desk in lexems.items():
#
        #            if lexem in prompt_units:
#
        #                if desk == sp.desk:
#
        #                    #print(f'{sp.desk}: {sp.value}')
#
        #                    strokes[strokes.index(stroke)] = ' ' * space_units_count + sp.get_space()
        #                    #print(' ' * space_units_count + sp.get_space())
#
        #        break
#
        #    elif ('[[' in stroke) and (']]' in stroke):
#
        #        space_units_count: int = len(stroke) - len(stroke.lstrip())
#
        #        strokes = '\n'.join(strokes).replace(stroke, ' ' * space_units_count + sp.get_space(), 1)
#
        #        strokes = strokes.split('\n')
#
        #        break
#
        #        #strokes[strokes.index(stroke)] = ' ' * space_units_count + sp.get_space()

        #with open(file='output.html', mode='w', encoding='UTF-8') as output:
#
        #    output.write('\n'.join(strokes))

        #print('********************')

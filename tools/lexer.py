from tools import parser, space, linker
import re
import json

class Lexer:

	@classmethod
	def __find_lexems(cls):

		for stroke in cls.strokes:

			'''Find a blocks'''

			func_block = re.findall(pattern=r'\[\$.{0,}\$\]', string=stroke) # re functional block

			var_block = re.findall(pattern=r'\[\[\s{0,}\$\w{0,}\s{0,}\]\]', string=stroke)# re variable block

			html_record: any

			if func_block:

				'''Find existing lexem in current block'''

				lexem_data: str

				for lexem, desk in cls.lexems.items():

					re_lexem = re.findall(pattern=f'({lexem})', string=func_block[0])

					if re_lexem: 

						lexem_data = {'lexem_value': lexem, 'lexem_type': desk}
						
						break

				if lexem_data['lexem_type'] == 'DEBUG':

					re_arg = re.findall(pattern=r'(?<=debug)\s{0,}\S{0,}\s{0,}(?=\$)', string=func_block[0])

					value = re_arg[0].strip()

					html_record = space.Space(desk=lexem_data['lexem_type'], value=value)

				elif lexem_data['lexem_type'] == 'LET':

					var_name = re.findall(pattern=r'(?<=let)\s{0,}\S{0,}\s{0,}(?=\=)', string=func_block[0])[0].strip()
					var_value = re.findall(pattern=r'(?<=\=)\s{0,}\S{0,}\s{0,}(?=\$)', string=func_block[0])[0].strip()

					html_record = space.Space(desk=lexem_data['lexem_type'], value=(var_name, var_value))

			elif var_block:

				...

			else:

				html_record = stroke

			record: str = html_record.get_space() if isinstance(html_record, space.Space) else html_record

			linker.Linker.Storage.write_template(template='base.html', stroke=record)

		parser.Parser.write()

		#print(linker.Linker.Storage.get_template_content(template='base.html'))




	def __new__(cls, strokes: list):
        
		cls.strokes: list = strokes

		cls.lexems: dict = json.loads(open(file='lexems.json', mode='r', encoding='UTF-8').read())

		cls.__find_lexems()

#Lexer(['[$ debug   gg hh $]', '[[ $GUI ]]'])
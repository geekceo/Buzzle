from tools import parser, space, linker
import re
import os
import json

class Lexer:

	LIB_DIR: str = os.path.dirname(p=__file__)

	@classmethod
	def __find_lexems(cls):

		error: bool = False
		error_temp: str = ''

		for index, stroke in enumerate(cls.strokes):

			'''Find a blocks'''

			func_block = re.findall(pattern=r'\[\$.{0,}\$\]', string=stroke) # re functional block

			var_block = re.findall(pattern=r'\[\[\s{0,}\$\w{0,}\s{0,}\]\]', string=stroke)# re variable block

			html_record: any

			if func_block:

				'''Find existing lexem in current block'''

				lexem_data: str = None

				for lexem, desk in cls.lexems.items():

					re_lexem = re.findall(pattern=f'({lexem})', string=func_block[0])

					if re_lexem: 

						lexem_data = {'lexem_value': lexem, 'lexem_type': desk}
						
						break

				if lexem_data == None:

					with open(file=f'{cls.LIB_DIR}/../docs/error_temp', mode='r') as file:

						error_temp = file.read()

					error_temp = error_temp.replace('{title}', f'Unknown command in line {index+1}: \"{func_block[0]}\"').replace('{info}', 'Bla\nBla\nBla')

					with open(file=f'{cls.LIB_DIR}/../docs/error.html', mode='w') as file:

						file.write(error_temp)

					error = True

					linker.Linker.Storage.init_templates(templates=[cls.template_name])

					break

				#print(stroke)

				if lexem_data['lexem_type'] == 'DEBUG':

					re_arg = re.findall(pattern=r'(?<=debug)\s{0,}\S{0,}\s{0,}(?=\$)', string=func_block[0])

					value = re_arg[0].strip()

					html_record = space.Space(template_name=cls.template_name, desk=lexem_data['lexem_type'], value=value)

				elif lexem_data['lexem_type'] == 'LET':

					var_value: str | int = ''

					var_name = re.findall(pattern=r'(?<=let)\s{0,}\S{0,}\s{0,}(?=\=)', string=func_block[0])[0].strip()
					var_value_string = re.findall(pattern=r'(?<=\=)\s{0,}\".{0,}\"\s{0,}(?=\$)', string=func_block[0])
					var_value_int = re.findall(pattern=r'(?<=\=)\s{0,}\d{0,}\s{0,}(?=\$)', string=func_block[0])

					if var_value_string:

						var_value = var_value_string[0].strip()

					elif var_value_int:

						var_value = var_value_int[0].strip()

					html_record = space.Space(template_name=cls.template_name, desk=lexem_data['lexem_type'], value=(var_name, var_value))

			elif var_block:

				for block in var_block:
					
					var_name = var_name = re.findall(pattern=r'(?<=\$)([^1-90 ]\w{0,})\b', string=block)[0].strip()

					var_value: str = ''

					if re.findall(pattern=f'(?<=\").{{0,}}\[\[ \${var_name} \]\].{{0,}}?(?=\")', string=stroke):

						var_value = linker.Linker.Storage.get_var(template_name=cls.template_name, key=var_name, conversion=True)

					else:
						var_value = linker.Linker.Storage.get_var(template_name=cls.template_name, key=var_name, conversion=False)

					#print(var_value)

					stroke = stroke.replace(block, var_value, 1)

				html_record = stroke

			else:

				html_record = stroke

			record: str = html_record.get_space() if isinstance(html_record, space.Space) else html_record

			#print(record)

			linker.Linker.Storage.write_template(template=cls.template_name, stroke=record)

		if error:

			for stroke in error_temp.split('\n'):

				linker.Linker.Storage.write_template(template=cls.template_name, stroke=stroke)

		#parser.Parser.write(temlate_name=cls.template_name)

		#print(linker.Linker.Storage.get_template_content(template='base.html'))




	def __new__(cls, strokes: list, template_name: str):
        
		cls.strokes: list = strokes

		cls.template_name = template_name

		cls.lexems: dict = json.loads(open(file='lexems.json', mode='r', encoding='UTF-8').read())

		cls.__find_lexems()

#Lexer(['[$ debug   gg hh $]', '[[ $GUI ]]'])
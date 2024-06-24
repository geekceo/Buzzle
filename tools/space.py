from tools import linker
import re
import os
import config
import json

LIB_DIR: str = os.path.dirname(p=__file__)

class Space:

    '''Create space by lexems desk'''
    def __create_space(self):

        space: str = ''

        #print(self.desk)

        if self.desk == 'DEBUG':

            innerText: str

            #print(self.value)

            ''' Find char '$' to check if variable '''

            var_name = re.findall(pattern=r'(?<=\$)([^1-90 ]\w{0,})\b', string=self.value)

            if var_name:

                innerText = linker.Linker.Storage.get_var(template_name=self.template_name, key=var_name[0])

            else:

                innerText = self.value


            space = f"<h1>{innerText}</h1>" # create debug tag via <h1>

        # Look for varible assignment
        elif self.desk == 'LET':

            key, value = self.value

            #print(f'{key} : {value}')

            linker.Linker.Storage.set_var(template_name=self.template_name, key=key, value=value)

            if config.VARIABLE_VIEW:

                space = f'<input type="hidden" id="var_{key}" name="{key}" value={value} />' # create hidden inpout for save var key and value for using by JS

        elif self.desk == 'NOTIFICATION':

            if f'{self.value}.json' in config.NOTIFICATIONS:

                notif_temp = open(file=f'{LIB_DIR}/../docs/notif_temp', mode='r').read()

                notif_data = json.load(open(file=f'{config.BASE_DIR}/notifications/{self.value}.json', mode='r', encoding='UTF-8'))

                notif_temp = notif_temp.replace('{title}', notif_data['title']).replace('{text}', notif_data['text']).replace('{icon}', notif_data['icon'])

                print(notif_temp)

                space = notif_temp

        #print(space)

        # if variable mech was founded
        #elif '[[' in self.desk:
#
        #    space = self.value
        #
        #print(space)

        return space

    def __init__(self, template_name: str, desk: str = 'DEBUG', value: any = None):

        self.desk: str = desk
        self.value: any = value
        self.template_name: str = template_name

        #print(f'{self.desk}: {self.value}')

        self.space = self.__create_space()

    def get_space(self):

        return self.space
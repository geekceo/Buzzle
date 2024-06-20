from tools import linker
import re


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

                innerText = linker.Linker.Storage.get_var(template_name='test.html', key=var_name[0])

            else:

                innerText = self.value


            space = f"<h1>{innerText}</h1>" # create debug tag via <h1>

        # Look for varible assignment
        elif self.desk == 'LET':

            key, value = self.value

            #print(f'{key} : {value}')

            linker.Linker.Storage.set_var(template_name='test.html', key=key, value=value)

            space = f'<input type="hidden" id="var_{key}" name="{key}" value={value} />' # create hidden inpout for save var key and value for using by JS

        #print(space)

        # if variable mech was founded
        elif '[[' in self.desk:

            space = self.value
        
        #print(space)

        return space

    def __init__(self, desk: str = 'DEBUG', value: any = None):

        self.desk: str = desk
        self.value: any = value

        #print(f'{self.desk}: {self.value}')

        self.space = self.__create_space()

    def get_space(self):

        return self.space
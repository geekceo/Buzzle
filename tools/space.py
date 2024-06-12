from tools import linker


class Space:

    '''Create space by lexems desk'''
    def __create_space(self):

        if self.desk == 'DEBUG':

            units: list = []

            for unit in self.value:

                '''Look for variables in text arg'''
                if '$' in unit:

                    unit = unit.replace('$', '') # remove var buzzle char to get var name

                    units.append(linker.Linker.Storage.get_var(key=unit)) # get var value

                else:

                    units.append(unit)

            self.space = f"<h1>{' '.join(units)}</h1>" # create debug tag via <h1>

        '''Look for varible assignment'''
        if self.desk == 'LET':

            key, value = self.value

            linker.Linker.Storage.set_var(key=key, value=value)

            self.space = f'<input type="hidden" name="{key}" value={value} />' # create hidden inpout for save var key and value for using by JS

    def __init__(self, desk: str = 'DEBUG', value: any = None):

        self.desk: str = desk
        self.value: any = value

        self.__create_space()

    def get_space(self):

        return self.space
from datetime import datetime

class User():
    def __init__(self, name, birthdate, location):
        self.name = name
        self.birthdate = birthdate
        self.location = location
        self.register_date = datetime.now()

    def birthdate_strpdate(self):
        return datetime.strptime(self.birthdate,'%d/%m/%Y')

    def register_date_strftime(self):
        return datetime.strftime(self.register_date, '%d/%m/%Y')

    def print_user(self):
        return f'''
        Name: {self.name}
        Registered since: {self.register_date_strftime()}
        Location: {self.location}
        -------------------------------------------
        '''
    def print_user_name(self):
        return f'{self.name}'
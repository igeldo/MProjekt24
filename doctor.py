from person import Person


class Doctor(Person):
    def __init__(self, title: str,  name: str, surname: str, birthdate: str,phoneNumber: int,  abbreviation: str, profession: str):
        super().__init__(name, surname, birthdate, abbreviation)
        self._profession = profession
        self._title = title

    def show_attributes(self):
        print('Behandelnder Arzt/ Ärztin: ')
        print('Titel: ', self._title)
        super().show_attributes()
        print('Fachrichtung:', self._profession)
        print('Telefon: ', self.phoneNumber)

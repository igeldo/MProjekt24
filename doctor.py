from person import Person

class Doctor(Person):
    def __init__(self, title: str, name: str, surname: str, birthdate: str, phoneNumber: int, abbreviation: str, profession: str):
        super().__init__(name, surname, birthdate, phoneNumber, abbreviation)
        self._profession = profession
        self._title = title

    def get_profession(self):
        return self._profession

    def get_title(self):
        return self._title

    def get_all(self):
        return [self._name, self._surname, self._birthdate, self._phoneNumber, self._abbreviation, self._profession, self._title]
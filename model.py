class Model:
    def __init__(self):
        self._Blutbilder = []
        self._persons = []

    def add_Blutbild(self, blutbild):
        self._Blutbilder.append(blutbild)

    def add_person(self, person):
        self._persons.append(person)

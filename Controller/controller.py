class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def display_persons(self):
        for person in self._model.get_Personen():
            self._view.display_person(person)

    def display_Blutbilder(self):
        for blutbild in self._model.get_Blutbilder():
            self._view.display_blutbild(blutbild)

    def start(self):
        self.display_persons()

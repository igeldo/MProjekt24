class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        # nimmt Referenzen auf das Model- und View-Objekt entgegen
        # Diese Referenzen werden in den Instanzvariablen _model und _view gespeichert,
        # um später darauf zugreifen zu können

    def display_persons(self):
        for person in self._model.get_Personen(): # ruft die get_Personen()-Methode des Model-Objekts auf,
                                                  # um eine Liste aller Personen zu erhalten.
            self._view.display_person(person)

    def display_Blutbilder(self):
        for blutbild in self._model.get_Blutbilder():
            self._view.display_blutbild(blutbild)

    def start(self): # Diese Methode ist der Startpunkt der Controller-Logik.
        self.display_persons() # ruft die display_persons()-Methode auf, um die Personen in der Benutzeroberfläche anzuzeigen

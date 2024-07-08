from Model.blutbild import Blutbild
from Model.patient import Patient


class Model:
    def __init__(self): #zwei leere Listen initialisiert, um Blutbilder und Personen zu speichern, die hinzugefügt werden.
        self._blutbilder = []
        self._persons = []

    def add_Blutbild(self, blutbild):
        self._blutbilder.append(blutbild)
        # nimmt ein blutbild-Objekt entgegen und fügt es der Liste self._blutbilder hinzu.
        # so können nach und nach verschiedene Blutbilder zugeordnet werden.

    def add_person(self, person):
        self._persons.append(person)

    def get_Personen(self):
        return self._persons
    #gibt die Liste self._persons zurück, die alle dem Objekt zugeordneten Personen enthält.

    def get_Blutbilder(self):
        return self._blutbilder

    def linkBlutbildtoPatient(self, blutbild: Blutbild):
        blutid = blutbild.getPatID()
        correctPerson = None
        for person in self._persons:
            if isinstance(person, Patient):
                if person.get_patient_id() == blutid:
                    correctPerson = person
                    break  # Patient gefunden, Schleife abbrechen

        if correctPerson:
            correctPerson.add_Blutbilder(blutbild)
            blutbild.setSex(correctPerson.get_sex())

        #stellt also eine Verknüpfung zwischen einem Blutbild-Objekt und dem
        #dazugehörigen Patient-Objekt her
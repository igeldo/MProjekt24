from Model.blutbild import Blutbild
from Model.patient import Patient


class Model:
    def __init__(self):
        self._Blutbilder = []
        self._persons = []

    def add_Blutbild(self, blutbild):
        self._Blutbilder.append(blutbild)

    def add_person(self, person):
        self._persons.append(person)

    def get_Personen(self):
        return self._persons

    def get_Blutbilder(self):
        return self._Blutbilder

    def linkBlutbildtoPatient(self, blutbild: Blutbild):
        id = blutbild.getPatID()
        correctPerson = None
        for person in self._persons:
            if isinstance(person, Patient):
                if person.get_patient_id() == id:
                    correctPerson = person
                    break  # Patient gefunden, Schleife abbrechen

        if correctPerson:
            correctPerson.add_Blutbilder(blutbild)
            blutbild.setSex(correctPerson.get_sex())

from blutbild import Blutbild
from patient import Patient
from person import Person


class Model:
    def __init__(self):
        self._Blutbilder = []
        self._persons = []

    def add_Blutbild(self, blutbild):
        self._Blutbilder.append(blutbild)

    def add_person(self, person):
        self._persons.append(person)

    def linkBlutbildtoPatient(self, patient: Patient, blutbild: Blutbild):
        patient.add_Blutbilder(blutbild)
        blutbild.setSex(patient.get_sex())

    def get_Blutbilder(self):
        return [blutbild for blutbild in self._Blutbilder]

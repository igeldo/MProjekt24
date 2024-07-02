from datetime import date

from Model.blutbild import Blutbild
from Model.doctor import Doctor
from Model.messwert import Messwert
from Model.normwert import Normwerte
from Model.patient import Patient


class ExampleData:

    def __init__(self, model):
        self._main_model = model


    def addDoctorData(self):
        doctor1 = Doctor('Prof. Dr.', 'Maral', 'Safadi', '1970-09-06', +4917765432109, 'MS', 'Internistin')
        self._main_model.add_person(doctor1)

    def addPatientData(self):
        patient1 = Patient('John', 'Doe', '1990-07-15', +4915123456789, 'JD', 'Keine', 'Fieber', 'Männlich')
        self._main_model.add_person(patient1)

        patient2 = Patient('Jane', 'Smith', '1985-03-20', +4916234567890, 'JS', 'Vorerkrankung am Herzen', 'Husten',
                           'Weiblich')
        self._main_model.add_person(patient2)

        patient3 = Patient('Harald', 'Mueller', '1980-05-25', +4917345678901, 'HM', 'Diabetes Typ II',
                           'Kopfschmerzen, Schwächegefühl', 'Männlich')
        self._main_model.add_person(patient3)


    def addBlutbilderData(self):
        blutbild1 = Blutbild('2024-04-02', 1)
        blutbild1.addMesswert(Messwert('HB', 9.0))
        blutbild1.addMesswert(Messwert('WBC', 6000))
        blutbild1.addMesswert(Messwert('RBC', 5.0))
        blutbild1.addMesswert(Messwert('PLT', 150000))

        self._main_model.add_Blutbild(blutbild1)
        self._main_model.linkBlutbildtoPatient(blutbild1)

        blutbild2 = Blutbild('2024-04-06', 1)
        blutbild2.addMesswert(Messwert('HB', 9.5))
        blutbild2.addMesswert(Messwert('WBC', 8000))
        blutbild2.addMesswert(Messwert('RBC', 6.0))
        blutbild2.addMesswert(Messwert('PLT', 300000))

        self._main_model.add_Blutbild(blutbild2)
        self._main_model.linkBlutbildtoPatient(blutbild2)

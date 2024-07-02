import unittest
from datetime import datetime
from Model.blutbild import Blutbild
from Model.messwert import Messwert
from Model.patient import Patient

class TestPatient(unittest.TestCase):
    def setUp(self):
        self.patient = Patient(
            name="John",
            surname="Doe",
            birthdate="1990-01-01",
            phoneNumber=123456789,
            abbreviation="JD",
            preIllness="Diabetes",
            symptoms="Headache, Fatigue",
            sex="Male"
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.get_name(), "John")
        self.assertEqual(self.patient.get_surname(), "Doe")
        self.assertEqual(self.patient.get_birthdate(), "1990-01-01")
        self.assertEqual(self.patient.get_phone_number(), 123456789)
        self.assertEqual(self.patient.get_abbreviation(), "JD")
        self.assertEqual(self.patient.get_preillness(), "Diabetes")
        self.assertEqual(self.patient.get_symptoms(), "Headache, Fatigue")
        self.assertEqual(self.patient.get_sex(), "Male")
        self.assertEqual(self.patient.get_patient_id(), 1)

    def test_add_blutbild(self):
        blutbild1 = Blutbild(
            Aufnahmedatum = "2024-02-02",
            PatID = 1
        )
        blutbild1.addMesswert(Messwert('HB', 9.0))
        blutbild1.addMesswert(Messwert('WBC', 6000))
        blutbild1.addMesswert(Messwert('RBC', 5.0))
        blutbild1.addMesswert(Messwert('PLT', 150000))


        self.patient.add_Blutbilder(blutbild1)


        self.assertEqual(len(self.patient.get_Blutbilder()), 1)
        self.assertEqual(self.patient.get_Blutbilder()[0].getMesswerte()[1], ('WBC',6000))


    def test_get_all(self):
        expected_output = [
            "John", "Doe", "1990-01-01", 123456789, "JD", "Diabetes",
            "Headache, Fatigue", "Male", 1
        ]
        self.assertListEqual(self.patient.get_all(), expected_output)

if __name__ == '__main__':
    unittest.main()
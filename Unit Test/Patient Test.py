import unittest
from datetime import datetime
from Model.blutbild import Blutbild
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
        self.assertEqual(self.patient.get_phoneNumber(), 123456789)
        self.assertEqual(self.patient.get_abbreviation(), "JD")
        self.assertEqual(self.patient.get_preillness(), "Diabetes")
        self.assertEqual(self.patient.get_symptoms(), "Headache, Fatigue")
        self.assertEqual(self.patient.get_sex(), "Male")
        self.assertEqual(self.patient.get_patient_id(), 1)

    def test_add_blutbild(self):
        blutbild1 = Blutbild(
            patient_id=self.patient.get_patient_id(),
            hemoglobin=14.5,
            erythrocytes=5.2,
            leukocytes=7.8,
            thrombocytes=250,
            date="2023-06-01"
        )
        blutbild2 = Blutbild(
            patient_id=self.patient.get_patient_id(),
            hemoglobin=15.0,
            erythrocytes=5.1,
            leukocytes=8.2,
            thrombocytes=275,
            date="2023-07-01"
        )

        self.patient.add_Blutbilder(blutbild1)
        self.patient.add_Blutbilder(blutbild2)

        self.assertEqual(len(self.patient.get_Blutbilder()), 2)
        self.assertEqual(self.patient.get_Blutbilder()[0].get_hemoglobin(), 14.5)
        self.assertEqual(self.patient.get_Blutbilder()[1].get_hemoglobin(), 15.0)

    def test_get_all(self):
        expected_output = [
            "John", "Doe", "1990-01-01", 123456789, "JD", "Diabetes",
            "Headache, Fatigue", "Male", 1
        ]
        self.assertListEqual(self.patient.get_all(), expected_output)

if __name__ == '__main__':
    unittest.main()
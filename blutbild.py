from datetime import date

from messwert import Messwert
from normwert import Normwerte


class Blutbild:
    def __init__(self, Aufnahmedatum: date, PatID: int):
        self._sex = None
        self._patID = PatID
        self._aufnahmedatum = Aufnahmedatum
        self._messwerte = []


    def addMesswert(self, messwert: Messwert):
        self._messwerte.append(messwert)

    def getPatID(self):
        return self._patID

    def getDate(self):
        return self._aufnahmedatum

    def getMesswerte(self):
        return [messwert.get_Messwert() for messwert in self._messwerte]

    def setSex(self, sexPatient):
        self._sex = sexPatient

    def checkMesswerte(self):
        results = []
        for messwert in self._messwerte:
            type, patientValue = messwert.get_Messwert()
            normwert = None
            if self._sex == "Männlich":
                normwert = Normwerte[type + "Male"].value
            elif self._sex == "Weiblich":
                normwert = Normwerte[type + "Female"].value

            if normwert:
                min_value = normwert.get_MinValue()
                max_value = normwert.get_MaxValue()
                if min_value <= patientValue <= max_value:
                    results.append((type, patientValue, "normal"))
                elif patientValue < min_value:
                    results.append((type, patientValue, "zu gering"))
                elif patientValue > max_value:
                    results.append((type, patientValue, "zu hoch"))

        return results

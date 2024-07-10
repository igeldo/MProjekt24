from datetime import date

from Model.messwert import Messwert
from Model.normwert import Normwerte


class Blutbild:
    def __init__(self, Aufnahmedatum: date, PatID: int):
        self._sex = None
        self._patID = PatID
        self._aufnahmedatum = Aufnahmedatum
        self._messwerte = []

    def addMesswert(self, messwert: Messwert): # nimmt ein Messwert-Objekt als Parameter entgegen.
        self._messwerte.append(messwert) # Sie fügt diesen Messwert der Liste _messwerte hinzu,
                                         # die zur Speicherung aller Messwerte eines Patienten dient.

    def addPatID(self, patID: int): # nimmt eine ganze Zahl (int) als Parameter, die die Patienten-ID darstellt.
        self._patID = patID # Sie weist den übergebenen Wert der Instanzvariable _patID zu, um die Patienten-ID für dieses Objekt zu speichern.

    def addAufnahmedatum(self, aufnahmedatum: date): # nimmt ein date-Objekt als Parameter, das das Aufnahmedatum des Patienten darstellt.
        self._aufnahmedatum = aufnahmedatum # Sie weist den übergebenen Wert der Instanzvariable _aufnahmedatum zu,
                                            # um das Aufnahmedatum für diesen Patienten zu speichern.

    def getPatID(self):
        return self._patID # gibt den Wert der Instanzvariable _patID zurück, die die Patienten-ID des Patienten enthält.

    def getDate(self):
        return self._aufnahmedatum # gibt den Wert der Instanzvariable _aufnahmedatum zurück, die das Aufnahmedatum des Patienten enthält.

    def getMesswerte(self): # nimmt keine Parameter an, sondern gibt stattdessen eine Liste von Messwerten des Patienten zurück
        return [messwert.get_Messwert() for messwert in self._messwerte]
        # gibt zwei Werten zurück: der erste Wert ist der Typ des Messwerts (z.B. "Blutzucker"),
        # der zweite Wert ist der eigentliche gemessene Wert.

    def setSex(self, sexPatient): # dient dazu, das Geschlecht des Patienten in der Klasse zu setzen.
        self._sex = sexPatient

    def clearAll(self): # alle wichtigen Felder der Klasse auf ihren Ausgangszustand zurückzusetzen, z.B. um einen neuen Patienten anzulegen.
        self._messwerte = []
        self._patID = None
        self._aufnahmedatum = None

# alle Messwerte des Patienten werden überprüft, ob sie im normalen Bereich liegen oder ob sie zu hoch oder zu niedrig sind.
    def checkMesswerte(self):
        results = [] # leere Liste, in der die Ergebnisse der Überprüfung gespeichert werden.
        for messwert in self._messwerte:
            blood_type, patientValue = messwert.get_Messwert()
            normwert = None
            if self._sex == "Männlich" or "männlich" or "male":
                normwert = Normwerte[blood_type + "Male"].value
            elif self._sex == "Weiblich" or "weiblich" or "female":
                normwert = Normwerte[blood_type + "Female"].value

            if normwert:
                min_value = normwert.get_MinValue()
                max_value = normwert.get_MaxValue()
                if min_value <= patientValue <= max_value:
                    results.append((blood_type, patientValue, "normal"))
                elif patientValue < min_value:
                    results.append((blood_type, patientValue, "zu gering"))
                elif patientValue > max_value:
                    results.append((blood_type, patientValue, "zu hoch"))

        return results

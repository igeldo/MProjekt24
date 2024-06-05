from datetime import date
from messwert import Messwert


class Blutbild:
    def __init__(self, Aufnahmedatum: date, PatID: int):
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
        return self._messwerte

from datetime import date
from messwert import Messwert


class Blutbild:
    def __init__(self, date, PatID: int):
        self._patID = PatID
        self._date = date
        self._messwerte = []

    def addMesswert(self, messwert: Messwert):
        self._messwerte.append(messwert)
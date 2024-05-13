from datetime import date

class Blutbild:
    def __init__(self, date, PatID: int):
        self._patID = PatID
        self._date = date
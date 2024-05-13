from blutbild import Blutbild
class Blutwert(Blutbild):
    def __init__(self, date, PatID: int, name: str, PatientValue: float):
        super().__init__(date, PatID)
        self._name = name
        self._PatientValue = PatientValue




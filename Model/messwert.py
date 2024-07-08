#Die Messwert-Klasse stellt einen einzelnen Messwert dar,
#der mit einem Patienten in Verbindung steht.
class Messwert:
    def __init__(self, type: str, patientValue: float):
        self._type = type
        self._patientValue = patientValue

    def get_Messwert(self):
        return self._type, self._patientValue



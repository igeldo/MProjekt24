from enum import Enum


class Normwert:
    def __init__(self, abbreviation: str, unit: str, normalValue_min: float, normalValue_max: float, shortDescription: str):
        self._abbreviation = abbreviation
        self._unit = unit
        self._normalValue_min = normalValue_min
        self._normalValue_max = normalValue_max
        self._short_Description = shortDescription

class Normwerte(Enum):
    HaemoglobinMale = Normwert('HB', 'mmol/l', 8.1, 10.5, 'transportiert Sauerstoff im Blut')
    HaemoglobinFemale = Normwert('HB', 'mmol/l', 7.4, 9.9, 'transportiert Sauerstoff im Blut')
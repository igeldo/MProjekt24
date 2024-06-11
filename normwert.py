from enum import Enum


class Normwert:
    def __init__(self, abbreviation: str, unit: str, normalValue_min: float, normalValue_max: float,
                 shortDescription: str):
        self._abbreviation = abbreviation
        self._unit = unit
        self._normalValue_min = normalValue_min
        self._normalValue_max = normalValue_max
        self._short_Description = shortDescription

    def get_MinValue(self):
        return self._normalValue_min

    def get_MaxValue(self):
        return self._normalValue_max


class Normwerte(Enum):
    HBMale = Normwert('HB', 'mmol/l', 8.1, 10.5, 'transportiert Sauerstoff im Blut')
    HBFemale = Normwert('HB', 'mmol/l', 7.4, 9.9, 'transportiert Sauerstoff im Blut')
    WBCMale = Normwert('WBC', '/u"\u03bcs"', 4000, 10000, 'wichtig für Immunsysthem')
    WBCFemale = WBCMale
    RBCMale = Normwert('RBC', 'Mio/u"\u03bcs"', 4.5, 5.9, 'zuständig für Sauerstofftransport')
    RBCFemale = Normwert('RBC', 'Mio/u"\u03bcs"', 4.1, 5.2, 'zuständig für Sauerstofftransport')
    PLTMale = Normwert('PLT', '/u"\u03bcl"', 1500000, 400000, 'Blutplättchen, zuständig für Blutgerinnung')
    PLTFemale = PLTMale
    HCTMale = Normwert('HCT', '%', 42, 50, 'feste Bestandteile im Blut')
    HCTFemale = Normwert('HCT', '%', 38, 44, 'feste Bestandteile im Blut')
    GLCMale = Normwert('GLC', 'mg/ dl', 70, 100, 'maßgeblich für die Energieversorgung')
    GLCFemale = GLCMale
    CRPMale = Normwert('CRP', 'mg/ dl', 'none', 0.5, 'Entzündungsmarker')
    CRPFemale = CRPMale
    KRMale = Normwert('KR', 'mg/ dl', 0.9, 1.3, 'Aussage zur Nierenfunktion')
    KRFemale = Normwert('KR', 'mg/ dl', 0.6, 1.1, 'Aussage zur Nierenfunktion')

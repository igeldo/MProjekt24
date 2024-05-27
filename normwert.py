from enum import Enum


class Normwert:
    def __init__(self, abbreviation: str, unit: str, normalValue_min: float, normalValue_max: float,
                 shortDescription: str):
        self._abbreviation = abbreviation
        self._unit = unit
        self._normalValue_min = normalValue_min
        self._normalValue_max = normalValue_max
        self._short_Description = shortDescription


class Normwerte(Enum):
    HaemoglobinMale = Normwert('HB', 'mmol/l', 8.1, 10.5, 'transportiert Sauerstoff im Blut')
    HaemoglobinFemale = Normwert('HB', 'mmol/l', 7.4, 9.9, 'transportiert Sauerstoff im Blut')
    LeukozytenMale = Normwert('WBC', '/u"\u03bcs"', 4000, 10000, 'wichtig für Immunsysthem')
    LeukozytenFemale = LeukozytenMale
    ErythrozytenMale = Normwert('RBC', 'Mio/u"\u03bcs"', 4.5, 5.9, 'zuständig für Sauerstofftransport')
    ErythrozytenFemale = Normwert('RBC', 'Mio/u"\u03bcs"', 4.1, 5.2, 'zuständig für Sauerstofftransport')
    ThrombozytenMale = Normwert('PLT', '/u"\u03bcl"', 1500000, 400000, 'Blutplättchen, zuständig für Blutgerinnung')
    ThrombozytenFemale = ThrombozytenMale
    HämatokritMale = Normwert('HCT', '%', 42,50,'feste Bestandteile im Blut')
    HämatokritFemale = Normwert('HCT', '%', 38,44,'feste Bestandteile im Blut')
    GlukoseMale = Normwert('GLC', 'mg/ dl', 70, 100, 'maßgeblich für die Energieversorgung')
    GlukoseFemale = GlukoseMale
    CProteinMale = Normwert('CRP', 'mg/ dl', 'none', 0.5,'Entzündungsmarker')
    CProteinFemale = CProteinMale
    KreatininMale = Normwert('KR', 'mg/ dl',0.9 , 1.3,'Aussage zur Nierenfunktion')
    KreatininFemale = Normwert('KR', 'mg/ dl',0.6 , 1.1,'Aussage zur Nierenfunktion')


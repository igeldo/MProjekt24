from Model.blutbild import Blutbild
from Model.person import Person


class Patient(Person):
    patient_counter = 0

    def __init__(self, name: str, surname: str, birthdate: str, phoneNumber: int, abbreviation: str, preIllness: str,
                 symptoms: str, sex: str): #nimmt mehrere Parameter entgegen, die zur Initialisierung des Objekts verwendet werden.

        super().__init__(name, surname, birthdate, phoneNumber, abbreviation) #Konstruktor für die Basiseigenschaften des Patienten

        self._preillness = preIllness #Hier wird die Instanzvariable _preillness mit dem übergebenen preIllness Wert initialisiert.
        self._symptoms = symptoms
        self._sex = sex
        Patient.patient_counter += 1 #Hier wird die Patienten-ID des Objekts
                                    # auf den aktuellen Wert des Klassenzählers gesetzt.
        self._patient_id = Patient.patient_counter
        self._Blutbilder = [] #Hier wird eine leere Liste _Blutbilder initialisiert,
            # die später zur Speicherung von Blutwerten des Patienten verwendet werden kann.


    #Erweiterung der Funktionalität der Patient-Klasse und der Zugriff auf
    #verschiedene Eigenschaften und Informationen eines Patienten-Objekts

    def add_Blutbilder(self, blutbild: Blutbild):
        self._Blutbilder.append(blutbild)
    #Diese Methode fügt ein neues Blutbild-Objekt zur Liste _Blutbilder des Patienten-Objekts hinzu.

    def get_preillness(self):
        return self._preillness
    #Diese Methode gibt den Wert der Instanzvariable _preillness (Vorerkrankungen) des Patienten-Objekts zurück.

    def get_symptoms(self):
        return self._symptoms

    def get_sex(self):
        return self._sex

    def get_patient_id(self):
        return self._patient_id

    def get_Blutbilder(self):
        return [blutbild for blutbild in self._Blutbilder]


    def get_all(self):
        return [self._name, self._surname, self._birthdate, self._phoneNumber, self._abbreviation, self._preillness,
                self._symptoms, self._sex, self._patient_id]
    #Diese Methode gibt eine Liste mit allen Attributen des Patienten-Objekts zurück,
    #einschließlich der von der Elternklasse geerbten Attribute.

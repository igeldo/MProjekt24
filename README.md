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

Wobei das Geschlecht automatisch bestimmt wird, sobald das Blutbild einem Patienten zugeordnet wird. Die Messwerte
werden dem Blutbild im Laufe der Anwendung zu geordnet und hier gespeichert.

Messwerte verfügen jeweils über

- Typ
- Wert

Die möglichen Typen und die dazugehörigen Normwerte sind in einer seperaten Klassse „normwert“ gespeichert.

```
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
    WBCMale = Normwert('WBC', '/u"\u03bcs"', 4000, 10000, 'wichtig für Immunsystem')
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

```

Alle Klassen verfügen über Getter-Methoden um die einzelnen Attribute auszugeben.
Die Klasse Blutbild verfügt weiterhin über eine Methode die die Patientenwerte mit den Normwerten abgleicht und angibt
ob die Patientenwerte zu hoch oder zu niedrig sind.

```
    def checkMesswerte(self):
        results = []
        for messwert in self._messwerte:
            blood_type, patientValue = messwert.get_Messwert()
            normwert = None
            if self._sex == "Männlich":
                normwert = Normwerte[blood_type + "Male"].value
            elif self._sex == "Weiblich":
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

```

In der Klasse „Model“ werden die einzelnen Personen und Blutbilder gespeichert und über eine Funktion miteinander
verbunden. Dafür wird die ID genutzt.

### View

Die Viewklassen sind für die Erstellung und Gestaltung der Benutzeroberfläche verantwortlich. In diesen Klassen wird das
Design der Oberfläche definiert, d.h. es wird festgelegt, welche Komponenten wie Textfelder, Buttons oder andere
Steuerelemente das Layout enthalten soll und wie diese angeordnet werden.

```
class App(QWidget):
    def __init__(self, controllergui: controllerGUI, view: ViewGUI):
        super().__init__()
        self._title = 'Krankenhaus Verwaltung'
        self._controller = controllergui
        self._view = view
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self._title)

        # Hauptlayout
        main_layout = QHBoxLayout()

        # Layout für die Eingabefelder und Buttons
        left_layout = QVBoxLayout()

        self.label1 = QLabel('Patienten ID:', self)
        left_layout.addWidget(self.label1)

        self.entry1 = QLineEdit(self)
        left_layout.addWidget(self.entry1)

        self.label2 = QLabel('Aufnahmedatum (YYYY-MM-DD):', self)
        left_layout.addWidget(self.label2)

        self.entry2 = QLineEdit(self)
        left_layout.addWidget(self.entry2)

        self.label3 = QLabel('Messwert Typ:', self)
        left_layout.addWidget(self.label3)

        self.entry3 = QLineEdit(self)
        left_layout.addWidget(self.entry3)

        self.label4 = QLabel('Messwert Wert:', self)
        left_layout.addWidget(self.label4)

        self.entry4 = QLineEdit(self)
        left_layout.addWidget(self.entry4)

        self.addButton1 = QPushButton('Messwert speichern', self)
        self.addButton1.clicked.connect(self.handle_add_Messwert)
        left_layout.addWidget(self.addButton1)

        self.addButton2 = QPushButton('Blutbild hinzufügen', self)
        self.addButton2.clicked.connect(self.handle_add_blutbild)
        left_layout.addWidget(self.addButton2)

        self.displayButton = QPushButton('alle Daten anzeigen', self)
        self.displayButton.clicked.connect(self.handle_display_allData)
        left_layout.addWidget(self.displayButton)

        self.addButton3 = QPushButton('neue Person anlegen', self)
        self.addButton3.clicked.connect(self.handle_create_person)
        left_layout.addWidget(self.addButton3)

        right_layout = QHBoxLayout()

        self.resultLabel = QLabel('', self)
        self.resultLabel.setWordWrap(True)
        self.resultLabel.setStyleSheet("border: 1px solid black; padding: 10px;")  # Rahmen und Polsterung hinzufügen
        right_layout.addWidget(self.resultLabel)

        # Füge die beiden Layouts zum Hauptlayout hinzu
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)
        self.show()

```

Zusätzlich ist in den Viewklassen auch die Erstellung des "schwarzen Rahmens" auf der rechten Seite der
Benutzeroberfläche enthalten, der initial leer ist. Die genaue Darstellung des Layouts ist in Abbildung 1 visualisiert.
Zusammenfassend lässt sich sagen, dass die Viewklassen die grafische Darstellung und Interaktionsmöglichkeiten der
Benutzeroberfläche definieren und implementieren, um dem Anwender eine intuitive und benutzerfreundliche Oberfläche zur
Verfügung zu stellen.

Alternativ gibt es auch eine View Klasse welche alle aktuellen Patientendaten und Blutbilder in der PyCharm-Konsole
ausgeben kann.

### Controller

Die Controller-Klassen hingegen dienen als Schnittstelle zwischen dem Modell und der grafischen Benutzeroberfläche. Sie
ermöglicht das Hinzufügen von Blutbildern, Messwerten und Patienten zum Modell, verwaltet diese Daten und steuert den
Ablauf der Anwendung.
Es gibt jeweils einen Controller für die Steuerung der graphischen Oberfläche und einen zur Steuerung der
Kommando-Ausgabe.
Die Controller-Klasse für das GUI beinhaltet unter anderem die Logik, um auf Benutzereingaben zu reagieren. Beispielsweise wird in
diesen Klassen implementiert, dass bei Betätigung der Schaltflächen "alle Daten anzeigen" oder "neue Person anlegen" ein
neues Fenster geöffnet wird, um die entsprechenden Funktionalitäten bereitzustellen.

```
class ControllerGUI:
    def __init__(self, model: Model, view):
        self._model = model
        self._view = view

        self._blutbildneu = Blutbild(date(1999, 1, 1), 0)

    def add_blutbild(self, gui):
        try:
            patient_id = gui.entry1.text()
            pat_id = int(patient_id)
            aufnahmedatum = gui.entry2.text()

            if not (patient_id and aufnahmedatum):
                raise ValueError("Patienten ID und Aufnahmedatum müssen ausgefüllt sein.")

            self._blutbildneu.addPatID(pat_id)
            self._blutbildneu.addAufnahmedatum(date.fromisoformat(aufnahmedatum))
            self._model.add_Blutbild(self._blutbildneu)
            self._model.linkBlutbildtoPatient(self._blutbildneu)
            #            self._blutbildneu.clearAll()
            QMessageBox.information(gui, 'Erfolg', 'Blutbild erfolgreich hinzugefügt.')
        except ValueError as e:
            QMessageBox.critical(gui, 'Fehler', f'Fehler bei der Eingabe: {e}')
        except Exception as e:
            QMessageBox.critical(gui, 'Fehler', f'Unerwarteter Fehler: {e}')
            print(f"Fehler in add_blutbild: {e}")

    def add_Messwert(self, gui):
        try:
            messwert_type = gui.entry3.text()
            messwert_value = gui.entry4.text()
            messwert = float(messwert_value)

            if not (messwert_type and messwert_value):
                raise ValueError("Messwert Typ und Messwert Wert müssen ausgefüllt sein.")

            self._blutbildneu.addMesswert(Messwert(messwert_type, messwert))
            QMessageBox.information(gui, 'Erfolg', 'Messwert erfolgreich gespeichert.')
            self.clear_Messwertentries(gui)
        except ValueError as e:
            QMessageBox.critical(gui, 'Fehler', f'Fehler bei der Eingabe: {e}')
        except Exception as e:
            QMessageBox.critical(gui, 'Fehler', f'Unerwarteter Fehler: {e}')
            print(f"Fehler in add_Messwert: {e}")

    def clear_Messwertentries(self, gui):
        gui.entry3.clear()
        gui.entry4.clear()

    def create_person(self, gui):
        self.person_app = PersonApp(self, self._view)
        self.person_app.show()



    def add_Patient(self, gui):
        try:
            name = gui.entry1.text()
            surname = gui.entry2.text()
            birth_date = gui.entry3.text()
            phonenumber = gui.entry4.text()
            phonenumber_int = int(phonenumber)
            abbreviation = gui.entry5.text()
            preillness = gui.entry6.text()
            symptoms = gui.entry7.text()
            sex = gui.entry8.text()
            patient = Patient(name, surname, birth_date, phonenumber_int, abbreviation, preillness, symptoms, sex)
            self._model.add_person(patient)
            QMessageBox.information(gui, 'Erfolg', 'Patient erfolgreich hinzugefügt.')
            self.person_app.close()
        except ValueError as e:
            QMessageBox.critical(gui, 'Fehler', f'Fehler bei der Eingabe: {e}')
        except Exception as e:
            QMessageBox.critical(gui, 'Fehler', f'Unerwarteter Fehler: {e}')
            print(f"Fehler in add_Patient: {e}")

    def start(self):
        app = QApplication(sys.argv)
        ex = App(self, self._view)
        sys.exit(app.exec_())
```


## Zusammenfassung

Das in Python programmierte Krankenhausinformationssystem (KIS) wurde nach dem Model-View-Controller-Architekturmuster
entwickelt. Das Programm ermöglicht die Erfassung von Patientendaten und Blutbildern. Es können neue Messwerte
gespeichert, Blutbilder hinzugefügt, Daten angezeigt und neue Patienten angelegt werden. Das System verwendet eine
grafische Benutzeroberfläche, die durch Ziehen der Fensterränder vergrößert werden kann und verschiedene Steuersymbole
enthält. Darüber hinaus wurde ein Unit-Test für die "Patient"-Klasse erstellt, um deren Funktionalität zu überprüfen.

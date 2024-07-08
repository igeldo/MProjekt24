# Krankenhausinformationssystem (KIS)

## Einleitung:

In unserer Master-Projektarbeit haben wir ein Krankenhausinformationssystem (KIS) in Python programmiert. Das Projekt
wurde nach dem Prinzip des Model-View-Controller (MVC)-Architekturmusters entwickelt. Dazu wurde eine Benutzeroberfläche
entworfen.

## Benutzeroberfläche (GUI)

In der folgenden Abbildung wird die Benutzeroberfläche dargestellt.

![GUI1.jpg](Images\GUI1.jpg)

Abbildung 1: Grafikoberfläche des KIS-Systems

Die Benutzeroberfläche kann durch Ziehen der Fensterränder mit der Maus vergrößert werden. Oben rechts im Fenster
befinden sich drei Symbole: Ein schwarzer Strich minimiert das Fenster, ein Rechtecksymbol maximiert es, und ein Kreuz
schließt es (Abbildung 2 rot umrahmt). Im Kopfbereich des Fensters wird der Programmname "Krankenhaus Verwaltung"
angezeigt (Abbildung 2 grün umrahmt).

![GUI2.jpg](Images\GUI2.jpg)

Abbildung 2: Fenstersteuerung über Symbolleiste

Rechts im Hauptfenster befindet sich ein schwarzer Rahmen, der der Anzeige von Daten aus der Datenbank dient.
Die Position des Fensters lässt sich nach Bedarf anpassen, indem der Anwender es an der gewünschten Stelle positioniert.
Im KIS-Programm können folgende Patientendaten erfasst werden:

- Patienten-ID
- Aufnahmedatum 
- Messwertyp 
- Messwert

Zudem können Messwerte gespeichert, Blutbilder hinzugefügt, alle Daten angezeigt und neue Patienten angelegt werden.
Durch Betätigen der entsprechenden Schaltflächen wie "alle Daten anzeigen" oder "neue Person anlegen" werden dafür
separate Fenster geöffnet. Diese wird in Abbildungen 3 und 4 dargestellt.

![GUI3.jpg](Images\GUI3.jpg)

Abbildung 3: Nachdem betätigen der Schaltfläche "alle Daten anzeigen" wird dieses Fenster angezeigt.

![GUI4.jpg](Images\GUI4.jpg)

Abbildung 4: Nachdem betätigen der Schaltfläche "neue Person anlegen" wird dieses Fenster angezeigt.

Zusätzlich wurde ein Unit-Test für die "Patient"-Klasse erstellt, um deren Funktionalität zu überprüfen.

```
class TestPatient(unittest.TestCase):
    def setUp(self):
        self.patient = Patient(
            name="John",
            surname="Doe",
            birthdate="1990-01-01",
            phoneNumber=123456789,
            abbreviation="JD",
            preIllness="Diabetes",
            symptoms="Headache, Fatigue",
            sex="Male"
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.get_name(), "John")
        self.assertEqual(self.patient.get_surname(), "Doe")
        self.assertEqual(self.patient.get_birthdate(), "1990-01-01")
        self.assertEqual(self.patient.get_phone_number(), 123456789)
        self.assertEqual(self.patient.get_abbreviation(), "JD")
        self.assertEqual(self.patient.get_preillness(), "Diabetes")
        self.assertEqual(self.patient.get_symptoms(), "Headache, Fatigue")
        self.assertEqual(self.patient.get_sex(), "Male")
        self.assertEqual(self.patient.get_patient_id(), 1)

    def test_add_blutbild(self):
        blutbild1 = Blutbild(
            Aufnahmedatum="2024-02-02",
            PatID=1
        )
        blutbild1.addMesswert(Messwert('HB', 9.0))
        blutbild1.addMesswert(Messwert('WBC', 6000))
        blutbild1.addMesswert(Messwert('RBC', 5.0))
        blutbild1.addMesswert(Messwert('PLT', 150000))
        self.patient.add_Blutbilder(blutbild1)
        self.assertEqual(len(self.patient.get_Blutbilder()), 1)
        self.assertEqual(self.patient.get_Blutbilder()[0].getMesswerte()[1], ('WBC', 6000))
```

## Model-View-Controller Konzept (MVC)

Model-View-Controller (MVC) ist ein Entwurfsmuster zur Unterteilung einer Software in drei Komponenten Datenmodell (
Model), Ansicht (View) und Programmsteuerung (Controller), die miteinander interagieren. Das Muster kann sowohl als
Architekturmuster als auch als Entwurfsmuster eingesetzt werden. Die Trennung von Model, View und Controller ermöglicht
eine modulare und flexible Softwareentwicklung. Änderungen an einer Komponente haben in der Regel keine Auswirkungen auf
die anderen Komponenten. Dadurch wird die Wartbarkeit, Testbarkeit und Wiederverwendbarkeit der Anwendung erhöht.

1. Model: Das Model repräsentiert die Daten und die Kernfunktionalität der Anwendung. Es kümmert sich um die Verwaltung
   und Verarbeitung der Daten, ohne sich um die Darstellung oder Interaktion zu kümmern.
2. View: Die View ist für die visuelle Darstellung der Daten verantwortlich. Sie erhält die Daten vom Model und
   präsentiert sie dem Benutzer in einer geeigneten Form, z.B. als grafische Oberfläche.
3. Controller: Der Controller fungiert als Vermittler zwischen Model und View. Er nimmt Benutzereingaben entgegen,
   verarbeitet sie und aktualisiert dann das Model entsprechend. Anschließend informiert er die View über Änderungen im
   Model, damit diese die Darstellung aktualisieren kann.

### Model

In unserem Programm stellen die Model-Klassen die Grundbausteine dar. In diesen Klassen werden die spezifischen
Eigenschaften und Attribute von Patienten und Ärzten definiert. Bei der Aufnahme eines Patienten wird automatisch eine
eindeutige Patienten-ID generiert und das Alter des Patienten ebenfalls automatisch berechnet, basierend auf einem
integrierten Algorithmus.
Folgende Eigenschaften werden den Patienten zugeordnet:

- Name
- Nachname
- Geburtstag bzw. der Alter
- Telefonnummer bzw. Handynummer
- Abkürzung des Namens
- Vorkrankheit
- Symptome
- Geschlecht

Und folgende Eigenschaften werden den Ärtzten zugeordnet:

- Titel
- Name
- Nachname
- Geburtstag
- Telefonnummer bzw. Handynummer
- Abkürzung
- Profession

Weiterhin gibt es noch Model-Klassen für die Blutbilder so wie die einzelnen Messwerte die darin enthalten sein Können.

Ein Blutbild verfügt über die Eigenschaften:

- Aufnahmedatum
- ID
- Geschlecht
- Messwerte

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
Die Controller-Klasse für das GUI beinhaltet unter anderem die Logik, um auf Benutzereingaben zu reagieren.
Beispielsweise wird in
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


# MProjekt24 - Sommersemester 2024 Herzfrequenzanalyse

Programmiert von: Corinne, Fatima

## Überblick

Dieses Programm ist eine Python Applikation basierend auf dem Model-View-Controller (MVC) Prinzip. 
Das Programm wurde designend für die Analyse und Anzeige der Herzfrequenz. Die Anwendung erlaubt dem Nutzer personenbezogene Information einzugeben, die Herzfrequenzdaten aus einer Exceldatei zu importieren und verschiedene Analysen anzuwenden. Dabei kann die Ruhe- und Maximalherzfrequenz ermittelt werden, die Korrelation zwischen der Herzfrequenz und dem Alter sowie die mittlere Herzfrequenz pro Aktivität bestimmt werden. 

## Projektstruktur

Der Programmcode besteht aus vier Hauptkomponenten: 
1.	Model: Stellt die Daten und Berechnungen dar
2.	View: Präsentiert die verwerteten Daten dem Nutzer
3.	Controller: Verwaltet die Kommunikation zwischen Model und View
4.	Main: Laufen der Anwendung

### Model

Die Klasse „Person“ der Datei „model.py“ repräsentiert eine Person mit den Eigenschaften Name, Alter, Geschlecht und Fitnesslevel. Diese Klasse bietet Methoden an, welche auf Grundlage dieser Eigenschaften die Berechnung der Ruhe- und Maximalherzfrequenz ermöglichen. 
Bild?

### View

Die Klasse „HeartRateView“ der Datei „view.py“ ist verantwortlich für die Anzeige der Daten der Klasse Person. Dabei sind Methoden zur Anzeige von persönlichen Eigenschaften, Herzfrequenzdaten für selbstwählbare Daten, der Ergebnisse der Korrelationsanalyse und der Durchschnittlichen Herzfrequenz pro Aktivität enthalten.
Bild?

### Controller

Die Klasse „PersonController“ der Datei „controller.py“ fungiert als Vermittler zwischen dem Model und View. Sie übernimmt den Datenimport, die Analyse und die Kommunikation zwischen Model und View. 

### Main

Die „main.py“ Datei initialisiert das Model, View und den Controller. Dabei werden auch die Benutzereingaben und Datenverarbeitung verwaltet. 


## Anforderungen

Das Programm wurde mit Python 3.12 geschrieben. Es werden zusätzlich folgende Python Pakete benötigt:

* Numpy
* Pandas
* Matplotlib

Diese Pakete können mit: 
```shell
pip install numpy pandas matplotlib
```
installiert werden.

### Anwendung von Matplotlib
Bilder

### Format der Exeldatei

Bitte achten Sie darauf, dass die verwendete Exceldatei folgende Spalten enthält:

* ‚Date‘: Datum der Herzfrequenzmessung
* ‚Time‘: Zeit zu der die Herzfrequenz ermittelt wurde in folgendem Format: hh:mm:ss
* ‚HeartRate‘: die ermittelte Herzfrequenz in bpm
* ‚Activity‘: Die Aktivität, während die Herzfrequenz aufgenommen wurde

## Starten des Programms

Navigieren Sie zu den Projektordnern und lassen sie die Datei „main.py“ laufen. Sobald das Programm durchläuft, werden Sie dazu aufgefordert persönliche Daten (Name, Alter, Geschlecht, Fitnesslevel) der zu analysierenden Person einzugeben. Anschließend müssen sie den Dateipfad der Exceldatei (in welcher die Herzfrequenzdaten gespeichert sind) eingeben. Dies funktioniert auch per Copy-Paste. 	
Das Programm zeigt dann die persönlichen Eigenschaften an und gibt die berechnete Ruhe und Maximalherzfrequenz aus. Nun kann ein bestimmtes Datum (Angabe in folgendem Format: YYYY-MM-DD) ausgewählt werden für eine genauere Ansicht der Herzfrequenzdaten. Dafür werden Plots für die Herzfrequenz des ausgesuchten Datums, aller aufgenommenen Herzfrequenzdaten der Person und die durchschnittliche Herzfrequenz pro Aktivität ausgegeben.
Zum Starten des Programms kann folgender Code verwendet werden:
```shell
python main.py
```


## Unittes
Die Datei „Unit Test.py“ enthält einen Test für die korrekte Berechnung der Korrelation mit der im Code geschrieben Methode.
Für den Unittest werden die Python Packages 

* unittest
* Mock von unittest
* Pandas
* Numpy 
benötigt.

Die Methode „setUp“ initialisiert den Testkontext, indem eine Testperson und ein Mock-View erstellt werden.

Die Methode „test_analyze_correlation_with_numeric_data“ testet die Funktionalität der Korrelationsanalyse mit numerischen Daten.


## Kontakt

Bei Fragen oder Problemen können Sie unser gerne per E-Mail kontaktieren: [unsereMail@beispiel.de]()



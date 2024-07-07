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

### View

Die Klasse „HeartRateView“ der Datei „view.py“ ist verantwortlich für die Anzeige der Daten der Klasse Person. Dabei sind Methoden zur Anzeige von persönlichen Eigenschaften, Herzfrequenzdaten für selbstwählbare Daten, der Ergebnisse der Korrelationsanalyse und der Durchschnittlichen Herzfrequenz pro Aktivität enthalten.

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

![Heart Rate for Date](https://github.com/igeldo/MProjekt24/blob/CorinneFarnazFatima/Pictures/Heart%20rate%20for%20Date%20.png "Heart Rate for Date")
Die Herzfrequenz für das ausgewählte Datum wird als Liniendiagramm mit herzfrequenz über die Zeit ausgegeben

![Heart Rate over Time](https://github.com/igeldo/MProjekt24/blob/CorinneFarnazFatima/Pictures/Heart%20Rate%20over%20Time.png)
Alle gemessenen Herzfrequenzen werden über den gesamten gemessenen zeitraum in einem Liniendiagramm ausgegeben.

![Mean Heart Rate per Activity](https://github.com/igeldo/MProjekt24/blob/CorinneFarnazFatima/Pictures/Mean%20Heart%20Rate%20per%20Activity.png)
Dieses Balkendiagramm zeigt die mittlere Herzfrequenz pro gemessener Aktivität.

### Darstellung der Eingaben und Ausgaben des Programms

![Erste Eingabeaufforderung](https://github.com/igeldo/MProjekt24/blob/CorinneFarnazFatima/Pictures/Screenshot%202024-07-07%20143311.png)
Dieses Bild zeigt die erste Eingabeaufforderung nach Start des Programms. Die zu tätigen Eingaben sind in Grün dargestellt.
Nach erfolgter Eingabe der daten werden bereits die Ruhe- und Maximalherzfrequenz berechnet

![Eingabe spezifisches Datum](https://github.com/igeldo/MProjekt24/blob/CorinneFarnazFatima/Pictures/Screenshot%202024-07-07%20143348.png)
Dieses Bild zeigt die Eingabe eines spezifischen Datums für die Auswertung der Herzfrequenz. Dabei kann ein belibges datum gewählt werden, an welchem die Herzfrequenz aufgenommen wurde.
Die Ausgabe zeigt die erhobenen Werte, die Plots und die berechnete Korrelation der Daten an.

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

![Code setup](https://github.com/igeldo/MProjekt24/blob/CorinneFarnazFatima/Pictures/Screenshot%202024-07-07%20151330.png)
Dieses Bild zeigt das die Methode "setUp".

Die Methode „test_analyze_correlation_with_numeric_data“ testet die Funktionalität der Korrelationsanalyse mit numerischen Daten.

![Numerische Daten](https://github.com/igeldo/MProjekt24/blob/CorinneFarnazFatima/Pictures/Screenshot%202024-07-07%20151434.png)
Dieses Bild zeigt die numerischen Daten für den Unittest.


## Kontakt

Bei Fragen oder Problemen können Sie unser gerne per E-Mail kontaktieren: [unsereMail@beispiel.de]()



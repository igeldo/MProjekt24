# MProjekt24 - Sommersemester 2024

Cigdem und Jasper

### Einrichten des virtual environment 

Einmalig wird die virtuelle Umgebung für das Projekt eingerichtet:
```shell
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Starten des Programms

### Wechsel in virtual environment

Für jede neu geöffnete Shell muss einmalig in die virtuelle Umgebung gewechselt werden:
```shell
cd <pfad_zu_src>/MProjekt24
source venv/bin/activate
```

### Ausführen des Programms

```shell
python main.py
```

### Ausführen der Tests

Ausführen aller Unit-Tests im Verzeichnis 'tests'

```shell
pytest
```

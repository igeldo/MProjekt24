from controller import PersonController

def main():
    # Erstellen eines Controllers
    controller = PersonController('Corinne', 28, 'female', 'good')

    # Daten importieren
    controller.import_data('V0.1_HFdaten.xlsx')

    # Ruheherzfrequenz und maximale Herzfrequenz berechnen und ausgeben
    resting_heart_rate = controller.get_resting_heart_rate()
    max_heart_rate = controller.get_maximum_heart_rate()

    print(f"Resting Heart Rate: {resting_heart_rate} bpm")
    print(f"Maximum Heart Rate: {max_heart_rate} bpm")

    # Herzfrequenzdaten analysieren und anzeigen
    controller.analyze_heart_rate()

    # Korrelation analysieren und anzeigen
    controller.analyze_correlation()

if __name__ == '__main__':
    main()


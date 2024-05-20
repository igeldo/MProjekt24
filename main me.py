from controller import PersonController

def main():
    # Erstellen eines Controllers
    controller = PersonController('Corinne', 28, 'female', 'good')

    # Daten importieren
    controller.import_data('V0.1_HFdaten.xlsx')

    # Herzfrequenzdaten analysieren und anzeigen
    controller.analyze_heart_rate()

    # Korrelation analysieren und anzeigen
    controller.analyze_correlation()

if __name__ == '__main__':
    main()
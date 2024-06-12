
from Controller.controller import PersonController
from Model.model import Person
from View.view import HeartRateView


def main():
    model= Person("Corinne", 28, 'female', 'good')
    view = HeartRateView(model)
    controller = PersonController(model,view)

    # Daten importieren
    controller.import_data('V0.1_HFdaten.xlsx')

    # Eigenschaften der Person ausgeben
    properties = controller.get_properties()
    print(f"Name: {properties['Name']}")
    print(f"Age: {properties['Age']}")
    print(f"Sex: {properties['Sex']}")
    print(f"Fitness Level: {properties['Fitness Level']}")

    # Ruheherzfrequenz und maximale Herzfrequenz berechnen und ausgeben
    resting_heart_rate = controller.get_resting_heart_rate()
    max_heart_rate = controller.get_maximum_heart_rate()

    print(f"Resting Heart Rate: {resting_heart_rate} bpm")
    print(f"Maximum Heart Rate: {max_heart_rate} bpm")

    # Herzfrequenzdaten für ein bestimmtes Datum analysieren und anzeigen
    specific_date = '2023-08-20'  # Beispiel Datum, das angezeigt werden soll
    day_data = controller.get_heart_rate_data_for_date(specific_date)
    print(f"Heart Rate Data for {specific_date}:")
    print(day_data)

    # Herzfrequenzdaten analysieren und anzeigen
    controller.analyze_heart_rate()

    # Korrelation analysieren und anzeigen
    controller.analyze_correlation()

if __name__ == '__main__':
    main()



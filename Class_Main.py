from Class_Person import Person
import openpyxl

class Main:
    def run(self, combine_datetime,heart_rates):
        person1 = Person('Corinne', 28, 'female', 'good')
        person1.import_data('V0.1_HFdaten.xlsx') #Import von Exceldatei funktioniert noch nicht --> Frage!
        person1.analyze_heart_rate(combine_datetime, heart_rates)


if __name__ == '__main__':
    main = Main()
    main.run("2022-12-27 08:26:49.219717", 60) #beispiel für datetime

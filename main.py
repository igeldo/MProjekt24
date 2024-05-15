from person import Person


class Main:
    def run(self, combine_datetime,heart_rates):
        person1 = Person('Corinne', 28, 'female', 'good')
        person1.import_data('V0.1_HFdaten.xlsx')
        person1.analyze_heart_rate(combine_datetime, heart_rates)


if __name__ == '__main__':
    main = Main()
    main.run("22.08.2023", 117) #beispiel für datetime

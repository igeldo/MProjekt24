from Herzfrequenzanalyse import Person


class Main:

    person1 = Person('Corinne', 28, 'female', 'good')
    person1.import_data('v0.1_HFdaten')
    person1.Analyse_Herzfrequenz()
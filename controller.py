from model import Person
from view import HeartRateView

class PersonController:
    def __init__(self, name, age, sex, fitness_level):
        self.person = Person(name, age, sex, fitness_level)
        self.view = HeartRateView()

    def import_data(self, excel_datei):
        self.person.import_data(excel_datei)

    def analyze_heart_rate(self):
        self.view.plot_heart_rate(self.person.heart_rate_data)

    def analyze_correlation(self):
        self.view.plot_correlation(self.person.heart_rate_data)
        correlation = self.person.calculate_correlation()
        print(f"Correlation between Heart Rate and Activity: {correlation}")

    def get_resting_heart_rate(self):
        return self.person.resting_heart_rate()

    def get_maximum_heart_rate(self):
        return self.person.maximum_heart_rate()

    def get_properties(self):
        return self.person.get_properties()

    def get_heart_rate_data_for_date(self, date):
        return self.person.get_heart_rate_data_for_date(date)



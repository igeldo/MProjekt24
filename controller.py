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

    def analyze_heart_rate(self):
        self.view.plot_heart_rate(self.person.heart_rate_data)

    def analyze_correlation(self):
        self.view.plot_correlation(self.person.heart_rate_data)
        correlation = self.person.calculate_correlation()
        print(f"Correlation between Heart Rate and Activity: {correlation}")

    def analyze_heart_rate(self):
        self.view.plot_heart_rate(self.person.heart_rate_data)

    def analyze_correlation(self):
        self.view.plot_correlation(self.person.heart_rate_data)
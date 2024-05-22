from model import Person
from view import HeartRateView

class PersonController:
    def __init__(self,model,view):
        self._model=model
        self._view = view

    def import_data(self, excel_datei):
        self._model.import_data(excel_datei)

    def analyze_heart_rate(self):
        self._view.plot_heart_rate()

    def analyze_correlation(self):
        self._view.plot_correlation()
        correlation = self._model.calculate_correlation()
        print(f"Correlation between Heart Rate and Activity: {correlation}")

    def get_resting_heart_rate(self):
        return self._model.resting_heart_rate()

    def get_maximum_heart_rate(self):
        return self._model.maximum_heart_rate()

    def get_properties(self):
        return self._model.get_properties()

    def get_heart_rate_data_for_date(self, date):
        return self._model.get_heart_rate_data_for_date(date)



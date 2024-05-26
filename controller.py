import pandas as pd
from model import Person
from view import HeartRateView
import matplotlib.pyplot as plt

class PersonController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.data = None

    def import_data(self, file_path):
        try:
            self.data = pd.read_excel(file_path)
            print(f"Data imported successfully from {file_path}")
        except Exception as e:
            print(f"Error importing data: {e}")

    def get_properties(self):
        return {
            'Name': self.model.name,
            'Age': self.model.age,
            'Sex': self.model.sex,
            'Fitness Level': self.model.fitness_level
        }

    def get_resting_heart_rate(self):
        return 60  # Placeholder for resting heart rate

    def get_maximum_heart_rate(self):
        return 180  # Placeholder for maximum heart rate

    def get_heart_rate_data_for_date(self, date):
        if self.data is not None:
            day_data = self.data[self.data['Date'] == date]
            return day_data
        return None

    def analyze_correlation(self):
        if self.data is not None:
            correlation_matrix = self.data.corr()
            print("Correlation Matrix:")
            print(correlation_matrix)

def analyze_correlation(self):
    if self.data is not None:
        # Exclude columns with datetime.time data type
        numeric_data = self.data.select_dtypes()

        if not numeric_data.empty:
            correlation_matrix = numeric_data.corr()
            print("Correlation Matrix:")
            print(correlation_matrix)
        else:
            print("No numeric data available for correlation analysis.")

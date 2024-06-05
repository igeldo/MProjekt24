import numpy as np
import pandas as pd
from model import Person
from view import HeartRateView

class PersonController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.data = None

    def import_data(self, file_path):
        try:
            self.data = pd.read_excel(file_path)
            self.view.data = self.data  # Update the view with the imported data
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
        if self.model.sex == 'male':
            if self.model.age < 30:
                if self.model.fitness_level == 'excellent':
                    return 65
                elif self.model.fitness_level == 'good':
                    return 68
                elif self.model.fitness_level == 'low':
                    return 72
            elif 30 <= self.model.age < 50:
                if self.model.fitness_level == 'excellent':
                    return 67
                elif self.model.fitness_level == 'good':
                    return 70
                elif self.model.fitness_level == 'low':
                    return 74
            elif self.model.age >= 50:
                if self.model.fitness_level == 'excellent':
                    return 70
                elif self.model.fitness_level == 'good':
                    return 72
                elif self.model.fitness_level == 'low':
                    return 76
        elif self.model.sex == 'female':
            if self.model.age < 30:
                if self.model.fitness_level == 'excellent':
                    return 68
                elif self.model.fitness_level == 'good':
                    return 71
                elif self.model.fitness_level == 'low':
                    return 75
            elif 30 <= self.model.age < 50:
                if self.model.fitness_level == 'excellent':
                    return 70
                elif self.model.fitness_level == 'good':
                    return 73
                elif self.model.fitness_level == 'low':
                    return 77
            elif self.model.age >= 50:
                if self.model.fitness_level == 'excellent':
                    return 73
                elif self.model.fitness_level == 'good':
                    return 76
                elif self.model.fitness_level == 'low':
                    return 80

    def get_maximum_heart_rate(self):
        return 220 - self.model.age

    def get_heart_rate_data_for_date(self, date):
        if self.data is not None:
            day_data = self.data[self.data['Date'] == date]
            return day_data
        return None

    def analyze_correlation(self):
        if self.data is not None:
            numeric_data = self.data.select_dtypes(include=[np.number])
            if not numeric_data.empty:
                correlation_matrix = numeric_data.corr()
                self.view.display_correlation_analysis(correlation_matrix)
            else:
                print("No numeric data available for correlation analysis.")

    def calculate_mean_heart_rate_per_activity(self):
        if self.data is not None:
            mean_heart_rate_per_activity = self.data.groupby('Activity')['HeartRate'].mean()
            self.view.display_mean_heart_rate_per_activity(mean_heart_rate_per_activity)

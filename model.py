from datetime import datetime
import pandas as pd

class Person:
    def __init__(self, name, age, sex, fitness_level):
        self.name = name
        self.age = age
        self.sex = sex
        self.fitness_level = fitness_level
        self.heart_rate_data = pd.DataFrame()  # Leere DataFrame für Herzfrequenzdaten

    def import_data(self, excel_datei: str):
        df = pd.read_excel(excel_datei)
        self.heart_rate_data = df
        return self.heart_rate_data

    def resting_heart_rate(self):  # Definition der RuheHF für Geschlecht nach Alter und Fitnesslevel
        if self.sex == 'male':
            if self.age <= 25:
                if self.fitness_level == 'excellent':
                    return 61
                elif self.fitness_level == 'good':
                    return 69
                elif self.fitness_level == 'low':
                    return 81
            elif 25 < self.age <= 35:
                if self.fitness_level == 'excellent':
                    return 61
                elif self.fitness_level == 'good':
                    return 70
                elif self.fitness_level == 'low':
                    return 81
            elif 35 < self.age <= 45:
                if self.fitness_level == 'excellent':
                    return 62
                elif self.fitness_level == 'good':
                    return 70
                elif self.fitness_level == 'low':
                    return 82
            elif 45 < self.age <= 55:
                if self.fitness_level == 'excellent':
                    return 63
                elif self.fitness_level == 'good':
                    return 71
                elif self.fitness_level == 'low':
                    return 83
            elif 55 < self.age <= 65:
                if self.fitness_level == 'excellent':
                    return 61
                elif self.fitness_level == 'good':
                    return 67
                elif self.fitness_level == 'low':
                    return 81
        elif self.sex == 'female':
            if self.age <= 25:
                if self.fitness_level == 'excellent':
                    return 65
                elif self.fitness_level == 'good':
                    return 73
                elif self.fitness_level == 'low':
                    return 84
            elif 25 < self.age <= 35:
                if self.fitness_level == 'excellent':
                    return 64
                elif self.fitness_level == 'good':
                    return 72
                elif self.fitness_level == 'low':
                    return 82
            elif 35 < self.age <= 45:
                if self.fitness_level == 'excellent':
                    return 64
                elif self.fitness_level == 'good':
                    return 73
                elif self.fitness_level == 'low':
                    return 84
            elif 45 < self.age <= 55:
                if self.fitness_level == 'excellent':
                    return 65
                elif self.fitness_level == 'good':
                    return 73
                elif self.fitness_level == 'low':
                    return 83
            elif 55 < self.age <= 65:
                if self.fitness_level == 'excellent':
                    return 64
                elif self.fitness_level == 'good':
                    return 73
                elif self.fitness_level == 'low':
                    return 83

    def maximum_heart_rate(self):
        return 220 - self.age

    def add_heart_rate_data(self, date, time, heart_rate_data):
        combine_datetime = datetime.combine(date, time)
        self.heart_rate_data = self.heart_rate_data.append({
            'Date': combine_datetime,
            'HeartRate': heart_rate_data
        }, ignore_index=True)

    def calculate_correlation(self):
        if 'HeartRate' in self.heart_rate_data.columns and 'fitness_level' in self.heart_rate_data.columns:
            correlation = self.heart_rate_data[['HeartRate', 'fitness_level']].corr().iloc[0, 1]
            return correlation
        else:
            raise ValueError("HeartRate or fitness_level data is not available")
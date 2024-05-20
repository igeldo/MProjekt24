from datetime import datetime
import pandas as pd

class Person:
    def __init__(self, name, age, sex, fitness_level):
        self.name = name
        self.age = age
        self.sex = sex
        self.fitness_level = fitness_level
        self.heart_rate_data = pd.DataFrame()  # Leerer DataFrame für Herzfrequenzdaten

    def import_data(self, excel_datei: str):
        df = pd.read_excel(excel_datei)
        df['Date'] = pd.to_datetime(df['Date'])
        self.heart_rate_data = df
        return self.heart_rate_data

    def resting_heart_rate(self):
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

    def add_heart_rate_data(self, date, time, heart_rate_data, activity):
        combine_datetime = datetime.combine(date, time)
        self.heart_rate_data = self.heart_rate_data.append({
            'Date': combine_datetime,
            'HeartRate': heart_rate_data,
            'Activity': activity
        }, ignore_index=True)

    def calculate_correlation(self):
        if 'HeartRate' in self.heart_rate_data.columns and 'Activity' in self.heart_rate_data.columns:
            correlation = self.heart_rate_data[['HeartRate', 'Activity']].corr().iloc[0, 1]
            return correlation
        else:
            raise ValueError("HeartRate or Activity data is not available")

    def get_properties(self):
        return {
            'Name': self.name,
            'Age': self.age,
            'Sex': self.sex,
            'Fitness Level': self.fitness_level
        }

    def get_heart_rate_data_for_date(self, date):
        date = pd.to_datetime(date)
        day_data = self.heart_rate_data[self.heart_rate_data['Date'].dt.date == date.date()]
        if day_data.empty:
            return f"No data available for {date.date()}"
        return day_data




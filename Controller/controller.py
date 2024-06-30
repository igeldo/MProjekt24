import numpy as np
import pandas as pd


class PersonController:
    # initialize of PersonController
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.data = None

    def import_data(self, file_path):
        # Import from Excelsheet
        try:
            self.data = pd.read_excel(file_path) #Import Excelsheet
            self.view.data = self.data  # Update the view with the imported data
            print(f"Data imported successfully from {file_path}")
        except Exception as e:
            print(f"Error importing data: {e}")

    def get_heart_rate_data_for_date(self, date):
        #returns heartrate data for self chosen date
        if self.data is not None:
            day_data = self.data[self.data['Date'] == date]
            return day_data
        return None

    def analyze_correlation(self):
        # Calculates Correlation of the numeric Data for heartrate and age
        if self.data is not None:
            numeric_data = self.data.select_dtypes(include=[np.number])
            if not numeric_data.empty:
                correlation_matrix = numeric_data.corr()
                self.view.display_correlation_analysis(correlation_matrix)
            else:
                print("No numeric data available for correlation analysis.")

    def calculate_mean_heart_rate_per_activity(self):
        # calculates mean heart rate per activity
        if self.data is not None:
            mean_heart_rate_per_activity = self.data.groupby('Activity')['HeartRate'].mean()
            self.view.display_mean_heart_rate_per_activity(mean_heart_rate_per_activity)

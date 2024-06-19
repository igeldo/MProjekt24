import matplotlib.pyplot as plt
import pandas as pd

class HeartRateView:
    def __init__(self, model):
        self.model = model
        self.data = None

    def display_properties(self):
        properties = self.model.get_properties()
        print(f"Name: {properties['Name']}")
        print(f"Age: {properties['Age']}")
        print(f"Sex: {properties['Sex']}")
        print(f"Fitness Level: {properties['Fitness Level']}")

    def display_heart_rate(self):
        resting_heart_rate = self.model.get_resting_heart_rate()
        max_heart_rate = self.model.get_maximum_heart_rate()
        print(f"Resting Heart Rate: {resting_heart_rate} bpm")
        print(f"Maximum Heart Rate: {max_heart_rate} bpm")

    def display_heart_rate_data_for_date(self, date, data):
        print(f"Heart Rate Data for {date}:")
        if data is not None and not data.empty:
            print(data)
            if 'Time' in data.columns:
                data = data.copy() # avoids SettingWithCopyWarning
                data['DateTime'] = pd.to_datetime(data['Date'].astype(str) + ' ' + data['Time'].astype(str))
                plt.figure(figsize=(10, 6)) # Plot for heartrate of specific Date
                plt.plot(data['DateTime'], data['HeartRate'], label='Heart Rate')
                plt.xlabel('Time')
                plt.ylabel('Heart Rate (bpm)')
                plt.title(f'Heart Rate Data for {date}')
                plt.legend()
                plt.grid(True)
                plt.show()
            else:
                print("Data does not contain a 'Time' column for plotting.")
        else:
            print("No data available for this date.")

    def analyze_heart_rate(self, data):
        if data is not None:
            plt.figure(figsize=(10, 6))
            plt.plot(data['Date'], data['HeartRate'], label='Heart Rate')
            plt.xlabel('Date')
            plt.ylabel('Heart Rate (bpm)')
            plt.title('Heart Rate Over Time')
            plt.legend()
            plt.grid(True)
            plt.show()

    def display_correlation_analysis(self, correlation_matrix):
        print("Correlation Matrix:")
        print(correlation_matrix)

    def display_mean_heart_rate_per_activity(self, mean_heart_rate_per_activity):
        activities = mean_heart_rate_per_activity.index
        mean_heart_rates = mean_heart_rate_per_activity.values

        plt.figure(figsize=(10, 6))
        plt.bar(activities, mean_heart_rates)
        plt.xlabel('Activity')
        plt.ylabel('Mean Heart Rate (bpm)')
        plt.title('Mean Heart Rate per Activity')
        plt.xticks(rotation=45)
        plt.show()
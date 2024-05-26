import matplotlib.pyplot as plt
class HeartRateView:
    def __init__(self, model):
        self.model = model
        self.data = None

    def display_properties(self, properties):
        print(f"Name: {properties['Name']}")
        print(f"Age: {properties['Age']}")
        print(f"Sex: {properties['Sex']}")
        print(f"Fitness Level: {properties['Fitness Level']}")

    def display_heart_rate(self, resting_heart_rate, max_heart_rate):
        print(f"Resting Heart Rate: {resting_heart_rate} bpm")
        print(f"Maximum Heart Rate: {max_heart_rate} bpm")

    def display_heart_rate_data_for_date(self, date, data):
        print(f"Heart Rate Data for {date}:")
        if data is not None and not data.empty:
            print(data)
        else:
            print("No data available for this date.")

    def display_heart_rate_analysis(self):
        print("Displaying heart rate analysis plot...")

    def display_correlation_analysis(self):
        print("Displaying correlation analysis...")

    def analyze_heart_rate(self):
        if self.data is not None:
            plt.figure(figsize=(10, 6))
            plt.plot(self.data['Date'], self.data['HeartRate'], label='Heart Rate')
            plt.xlabel('Date')
            plt.ylabel('Heart Rate (bpm)')
            plt.title('Heart Rate Over Time')
            plt.legend()
            plt.grid(True)
            plt.show()

class HeartRateView:
    def __init__(self, model):
        self.model = model

    def display_properties(self, properties):
        print(f"Name: {properties['Name']}")
        print(f"Age: {properties['Age']}")
        print(f"Sex: {properties['Sex']}")
        print(f"Fitness Level: {properties['Fitness Level']}")

    def display_heart_rate(self, resting_heart_rate, max_heart_rate):
        print(f"Resting Heart Rate: {resting_heart_rate} bpm")
        print(f"Maximum Heart Rate: {max_heart_rate} bpm")

    def display_heart_rate_data_for_date(self, date, data):
        print(f"Heart Rate Data for {date}:")
        if data is not None and not data.empty:
            print(data)
        else:
            print("No data available for this date.")

    def display_heart_rate_analysis(self):
        print("Displaying heart rate analysis plot...")

    def display_correlation_analysis(self):
        print("Displaying correlation analysis...")

    def analyze_heart_rate(self):
        if self.data is not None:
            plt.figure(figsize=(10, 6))
            plt.plot(self.data['Date'], self.data['HeartRate'], label='Heart Rate')
            plt.xlabel('Date')
            plt.ylabel('Heart Rate (bpm)')
            plt.title('Heart Rate Over Time')
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            print("No data available for heart rate analysis.")

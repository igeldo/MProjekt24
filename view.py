import matplotlib.pyplot as plt
import seaborn as sns

class HeartRateView:
    @staticmethod
    def plot_heart_rate(data):
        plt.plot(data['Date'], data['HeartRate'])
        plt.xlabel('Date/Time')
        plt.ylabel('Heart Rate')
        plt.title('Heart Rate over Time')
        plt.show()

    @staticmethod
    def plot_correlation(data):
        data['Activity'] = data['Activity'].astype('category').cat.codes
        sns.scatterplot(data=data, x='HeartRate', y='Activity')
        plt.title('Correlation between Heart Rate and Activity')
        plt.xlabel('Heart Rate')
        plt.ylabel('Activity')
        plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

class HeartRateView:
    def __init__(self, model):
        self._model = model

    def plot_heart_rate(self):
        data=self._model.heart_rate_data
        plt.plot(data['Date'], data['HeartRate'])
        plt.xlabel('Date/Time')
        plt.ylabel('Heart Rate')
        plt.title('Heart Rate over Time')
        plt.show()


    def plot_correlation(self):
        data = self._model.heart_rate_data
        data['Activity'] = data['Activity'].astype('category').cat.codes
        sns.scatterplot(data=data, x='HeartRate', y='Activity')
        plt.title('Correlation between Heart Rate and Activity')
        plt.xlabel('Heart Rate')
        plt.ylabel('Activity')
        plt.show()


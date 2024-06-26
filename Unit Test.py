import unittest
from unittest.mock import Mock
import pandas as pd
import numpy as np
from Controller.controller import PersonController
from Model.model import Person


class Test_Correlation(unittest.TestCase):
    def setUp(self):
        self.model = Person(name="Test", age=30, sex="male", fitness_level="good")
        self.view = Mock()
        self.controller = PersonController(self.model, self.view)

    def test_analyze_correlation_with_numeric_data(self):
        # Create a DataFrame with numeric data
        data = pd.DataFrame({
            'HeartRate': [72, 75, 78, 80],
            'Age': [25, 30, 35, 40],
            'Activity': ['Running', 'Walking', 'Cycling', 'Swimming']
        })
        self.controller.data = data

        # Call the method from controller
        self.controller.analyze_correlation()

        expected_correlation_matrix = data.select_dtypes(include=[np.number]).corr()


        self.view.display_correlation_analysis.assert_called_with(expected_correlation_matrix)

    def test_analyze_correlation_with_no_numeric_data(self):
        # Create DataFrame with no numeric data
        data = pd.DataFrame({
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
            'Activity': ['Running', 'Walking', 'Cycling']
        })
        self.controller.data = data

        # Call method
        with self.assertLogs(level='INFO') as log:
            self.controller.analyze_correlation()

        self.assertIn("No numeric data available for correlation analysis.", log.output)

    def test_analyze_correlation_with_empty_data(self):
        # Create empty DataFrame
        data = pd.DataFrame()
        self.controller.data = data

        # Call the method
        with self.assertLogs(level='INFO') as log:
            self.controller.analyze_correlation()

        self.assertIn("No numeric data available for correlation analysis.", log.output)


if __name__ == '__main__':
    unittest.main()

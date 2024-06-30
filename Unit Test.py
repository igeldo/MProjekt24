import unittest
from unittest.mock import Mock
import pandas as pd
import numpy as np
from Controller.controller import PersonController
from Model.model import Person


class Test_Correlation(unittest.TestCase):
    def setUp(self):
        # Prepare test context
        self.model = Person(name="Test", age=30, sex="male", fitness_level="good")
        self.view = Mock() # Create Mock object
        self.controller = PersonController(self.model, self.view) # initialize Controller with Model and Mock-View

    def test_analyze_correlation_with_numeric_data(self):
        # Create a DataFrame with numeric data
        data = pd.DataFrame({
            'HeartRate': [72, 75, 78, 80],
            'Age': [25, 30, 35, 40],
            'Activity': ['Running', 'Walking', 'Cycling', 'Swimming']
        })
        self.controller.data = data # assign dataframe to controller

        # Call the method from controller
        self.controller.analyze_correlation()

        #define expected matrix
        expected_correlation_matrix = np.array([[1, 0.996], [0.996, 1]])

        # verify that method of Mock-View is called exactly once
        self.view.display_correlation_analysis.assert_called_once()
        # get actual_corralation_matrix from Mock call
        actual_correlation_matrix = self.view.display_correlation_analysis.call_args[0][0].values

        # Print both matrices
        print("Expected Correlation Matrix:\n", expected_correlation_matrix)
        print("Actual Correlation Matrix:\n", actual_correlation_matrix)

        # Compare the matrices element-wise using assertAlmostEqual
        rows, cols = expected_correlation_matrix.shape
        for i in range(rows):
            for j in range(cols):
                self.assertAlmostEqual(expected_correlation_matrix[i, j], actual_correlation_matrix[i, j], places=3)


if __name__ == '__main__':
    unittest.main()

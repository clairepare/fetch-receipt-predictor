import numpy as np
import unittest
from polynomial_regression import PolynomialRegression

class TestPolynomialRegression(unittest.TestCase):

    def test_basic_functionality(self):
        # a linear function y = 2x + 3
        x = np.array([1, 2, 3, 4])
        y = 2 * x + 3
        
        # fiting a degree 1 polynomial
        model = PolynomialRegression(degree=1)
        model.fit(x, y)
        predictions = model.predict(x)

        # the predictions should be close to the actual y values
        np.testing.assert_almost_equal(predictions, y)

    def test_higher_degree(self):
        # a quadratic function y = x^2 + 2x + 3
        x = np.array([1, 2, 3, 4])
        y = x**2 + 2*x + 3
        
        # fitting a degree 2 polynomial
        model = PolynomialRegression(degree=2)
        model.fit(x, y)
        predictions = model.predict(x)

        # the predictions should be close to the actual y values
        np.testing.assert_almost_equal(predictions, y)

    def test_zero_degree(self):
        # x and y are not correlated
        x = np.array([1, 2, 3, 4])
        y = np.array([5, 5, 5, 5])
        
        # fitting a degree 0 polynomial
        model = PolynomialRegression(degree=0)
        model.fit(x, y)
        predictions = model.predict(x)

        # the predictions should all be close to the mean of y
        np.testing.assert_almost_equal(predictions, np.mean(y))

# Run the tests
if __name__ == '__main__':
    unittest.main()

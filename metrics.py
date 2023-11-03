import numpy as np

def mean_squared_error(estimates, targets):

    """
    Mean squared error measures the average of the square of the errors (the
    average squared difference between the estimated values and what is 
    estimated. The formula is:

    #MSE = (1 / n) * \\sum_{i=1}^{n} (Y_i - Yhat_i)^2

    Args:
        estimates(np.ndarray): the estimated values (should be the same shape as targets)
        targets(np.ndarray): the ground truth values

    Returns:
        MSE(int): mean squared error calculated by above equation 
    """

    error = targets - estimates

    error_squared = error**2

    MSE = 1/estimates.shape[0] * np.sum(error_squared)

    return MSE
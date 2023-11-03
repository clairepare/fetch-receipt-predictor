import numpy as np
try:
    import matplotlib.pyplot as plt
except:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

class PolynomialRegression():

    degree = 0
    weights = 0
    targets = 0
    features = 0

    def __init__(self, degree):
        """
        This class takes as input "degree", which is the degree of the polynomial 
        used to fit the data. For example, degree = 2 would fit a polynomial of the 
        form:

            ax^2 + bx + c
        
        Usage:
            learner = PolynomialRegression(degree = 1)
        Args:
            degree (int): Degree of polynomial used to fit the data.
        """
        self.degree = degree
    
    def fit(self, features, targets):
        """
        Fit the given data using a polynomial. The degree is given by self.degree,
        which is set in the __init__ function of this class. The goal of this
        function is fit features, a 1D numpy array, to targets, another 1D
        numpy array.

        Fit uses a vandermonde matrix. The Vandermonde matrix is constructed by taking the 
        values of the points and raising them to the powers from 0 to d, the degree
        of the polynomial.
        For degree 2, the matrix looks like:
                    [1 x1 x1^2]
                X=  [1 x2 x2^2]
                    [.........]
                    [1 xn xn^2]
        Args:
            features (np.ndarray): 1D array containing real-valued inputs.
            targets (np.ndarray): 1D array containing real-valued targets.
        Returns:
            None (saves model and training data internally)
        """

        #compute the vandermonde matrix, which is of the form [1 x x^2 ... x^n] for each feature
        vander_mtx = np.zeros((features.shape[0], self.degree + 1))
        for i in range(features.shape[0]):
            for j in range(self.degree + 1):
                vander_mtx[i, j] = features[i]**j

        self.targets = targets
        self.features = features

        #solve the equation (X.T*X)x = (X.T)y for the targets values to get the weights or coefficients of the polynomial
        self.weights = np.linalg.solve(np.dot(vander_mtx.T, vander_mtx), np.dot(vander_mtx.T, targets))

        return

    def predict(self, features):
        """
        Given features, a 1D numpy array, use the trained model to predict target 
        estimates. Call this after calling fit.
        Uses the weights (coeffs) and the given features to make an array of predictions

        Args:
            features (np.ndarray): 1D array containing real-valued inputs.
        Returns:
            predictions (np.ndarray): Output of saved model on features.
        """
        predictions = np.zeros(features.shape[0])
        for i in range(features.shape[0]):
            for j in range(self.weights.shape[0]):
                predictions[i] += self.weights[j] * features[i]**j  #add coefficients * corresponding x value raised to the jth power

        return predictions
    def visualize_full(self, degree, train_features, train_targets, test_features, test_targets, predictions):
        """
        This function should produce a single plot containing:
        - A scatter plot of the training features and targets
        - A scatter plot of the testing features and targets
        - The polynomial fit by the model graphed on top of the points

        Args:
            train_features (np.ndarray): 1D array containing real-valued inputs for training.
            train_targets (np.ndarray): 1D array containing real-valued targets for training.
            test_features (np.ndarray): 1D array containing real-valued inputs for testing.
            test_targets (np.ndarray): 1D array containing real-valued targets for testing.
            predictions (np.ndarray): 1D array containing model predictions on testing data.
        Returns:
            None (plots to the active figure)
        """
        #show predicted values if those exist as red x's
        if len(test_features) > 0 and len(predictions) > 0:
            plt.scatter(test_features, predictions, label='Predicted Data', color='red', marker='x')
        #if testing data exists show as green o's
        if len(test_targets) > 0:
            plt.scatter(test_features, test_targets, label='Actual Testing Data', color='green', marker='o')
        #show training data as blue circles
        plt.scatter(train_features, train_targets, label='Training Data', color='blue')

        if len(test_features) > 0 and len(predictions) > 0:
            poly_x = np.linspace(min(train_features), max(test_features), 100)
        else:
            poly_x = np.linspace(min(train_features), max(train_features), 100)
        poly_y = np.zeros(len(poly_x))
        for i in range(len(poly_x)):
            for j in range(self.weights.shape[0]):
                poly_y[i] += self.weights[j] * poly_x[i]**j  

        #plot figure and add labels
        plt.plot(poly_x, poly_y, label='Polynomial Fit', color='black')
        plt.legend()
        plt.xlabel('Month Number')
        plt.ylabel('Receipt Count')
        plt.title(f"Monthly Receipt Counts with Polynomial Fit of Degree {degree}")

        #save figure to display as output and close plot
        plt.savefig("static/output.png")
        plt.close()
        #plt.show()
        
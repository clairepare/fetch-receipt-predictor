import pandas as pd
import numpy as np

#reads the csv file with a given file path name and returns a new Dataframe
def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['# Date'])
    return df

def preprocess_data(df, train_ratio=0.7, use_all_data_for_training=True):
    """
        This method takes as input the loaded dataframe, a boolean that determines if
        all of the data is going to be used for training, and a ratio of the training/testing
        data.
        
        Usage:
            learner = PolynomialRegression(degree = 1)
        Args:
            df (DataFrame) = the data packaged in a DataFrame
            train_ratio (float) = the ratio of training to testing data, with 1 being all training data
            use_all_data_for_training (boolean) = whether all the data should be used for training
        Returns:
            train_data (list), test_data (list): the training and testing (if applicable).
        """

    if use_all_data_for_training:
        #grab the data into training data based on date
        train_data = df.resample('M', on='# Date').sum()
        test_data = pd.DataFrame(columns=train_data.columns)  #test data is empty
    else:
        #separate into training and testing data randomly, satisfying the train_ratio, for each month
        df['is_train'] = False
        for month in df['Month'].unique():
            idx = df[df['Month'] == month].index
            is_train = np.random.choice([True, False], size=len(idx), p=[train_ratio, 1-train_ratio])
            df.loc[idx, 'is_train'] = is_train

        train_data = df[df['is_train']].resample('M', on='# Date').sum()
        test_data = df[~df['is_train']].resample('M', on='# Date').sum()

    #create month number feature which will be plotted against receipt counts
    train_data['Month_Number'] = range(1, len(train_data) + 1)
    test_data['Month_Number'] = range(1, len(test_data) + 1)

    return train_data, test_data

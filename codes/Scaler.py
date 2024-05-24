import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class Scaler:
    def __init__(self, file_path):
        """
        Initialize with the path to the CSV file.
        """
        self.data = pd.read_csv(file_path)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_colwidth', None)

    def standardize_data(self):
        """
        Standardize the 'Budget in USD' and 'Rating' columns using StandardScaler.
        """
        scaled_data = self.data.copy()
        scaler = StandardScaler()
        scaled_data[['Budget in USD', 'Rating']] = scaler.fit_transform(scaled_data[['Budget in USD', 'Rating']])
        return scaled_data

    def normalize_data(self):
        """
        Normalize the 'Budget in USD' and 'Rating' columns using Min-Max Scaler.
        """
        normalized_data = self.data.copy()
        scaler = MinMaxScaler()
        normalized_data[['Budget in USD', 'Rating']] = scaler.fit_transform(normalized_data[['Budget in USD', 'Rating']])
        return normalized_data

    def get_data(self):
        """
        Return the processed DataFrame.
        """
        return self.data

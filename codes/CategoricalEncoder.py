import numpy as np
import pandas as pd
from codes import DateManagement 

class CategoricalEncoder:
    def __init__(self, file_path):
        """
        Initialize with the path to the CSV file.
        """
        self.data = pd.read_csv(file_path)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_colwidth', None)

    def encode_categorical(self):
        """
        One-hot encode categorical columns (Genre, Shooting Location).
        Ensure all one-hot encoded columns are integers (0 and 1).
        """
        self.data = pd.get_dummies(self.data, columns=['Genre', 'Shooting Location'])
        one_hot_columns = self.data.columns[self.data.dtypes == 'bool']
        self.data[one_hot_columns] = self.data[one_hot_columns].astype(int)
        return self.data

    
    def process_dates(self):
        """
        Process dates using DateManagement module.
        """
        self.data = DateManagement.DateManagement.process_dates(self.data)
        return self.data


    def get_data(self):
        """
        Return the processed DataFrame.
        """
        return self.data

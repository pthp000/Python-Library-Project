import pandas as pd
import numpy as np

class OutlierHandler:
    def __init__(self, file_path):
        """
        Initialize with the path to the CSV file.
        """
        self.data = pd.read_csv(file_path)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_colwidth', None)

    def identify_outliers(self):
        """
        Identify outliers in the dataset for 'Rating' and 'Budget in USD' columns using IQR method.
        """
        Q1_rating = self.data['Rating'].quantile(0.25)
        Q3_rating = self.data['Rating'].quantile(0.75)
        IQR_rating = Q3_rating - Q1_rating
        lower_limit_rating = Q1_rating - 1.5 * IQR_rating
        upper_limit_rating = Q3_rating + 1.5 * IQR_rating

        Q1_budget = self.data['Budget in USD'].quantile(0.25)
        Q3_budget = self.data['Budget in USD'].quantile(0.75)
        IQR_budget = Q3_budget - Q1_budget
        lower_limit_budget = Q1_budget - 1.5 * IQR_budget
        upper_limit_budget = Q3_budget + 1.5 * IQR_budget

        outliers = self.data[(self.data['Rating'] < lower_limit_rating) | 
                             (self.data['Rating'] > upper_limit_rating) | 
                             (self.data['Budget in USD'] < lower_limit_budget) | 
                             (self.data['Budget in USD'] > upper_limit_budget)]

        return outliers

    def correct_outliers(self):
        """
        Correct outliers by removing them from the dataset.
        """
        Q1_rating = self.data['Rating'].quantile(0.25)
        Q3_rating = self.data['Rating'].quantile(0.75)
        IQR_rating = Q3_rating - Q1_rating
        lower_limit_rating = Q1_rating - 1.5 * IQR_rating
        upper_limit_rating = Q3_rating + 1.5 * IQR_rating

        Q1_budget = self.data['Budget in USD'].quantile(0.25)
        Q3_budget = self.data['Budget in USD'].quantile(0.75)
        IQR_budget = Q3_budget - Q1_budget
        lower_limit_budget = Q1_budget - 1.5 * IQR_budget
        upper_limit_budget = Q3_budget + 1.5 * IQR_budget

        df_no_outliers = self.data[(self.data['Rating'] > lower_limit_rating) & 
                                   (self.data['Rating'] < upper_limit_rating) & 
                                   (self.data['Budget in USD'] > lower_limit_budget) & 
                                   (self.data['Budget in USD'] < upper_limit_budget)]

        return df_no_outliers

    def get_data(self):
        """
        Return the processed DataFrame.
        """
        return self.data

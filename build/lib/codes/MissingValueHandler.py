import pandas as pd
import numpy as np

class MissingValueHandler:
    def __init__(self, file_path):
        """
        Initialize with the path to the CSV file.
        """
        self.data = pd.read_csv(file_path)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_colwidth', None)

    def check_missing_values(self):
        """
        Check for missing values in the DataFrame.
        """
        return self.data.isnull().sum().sum()

    def fill_missing_with_mean(self):
        """
        Fill NaN values in 'Budget in USD' column with the mean.
        """
        mean_budget = np.nanmean(self.data['Budget in USD'])
        self.data['Budget in USD'] = self.data['Budget in USD'].fillna(mean_budget)
        return self.data

    def fill_missing_with_median(self):
        """
        Fill NaN values in 'Budget in USD' column with the median.
        """
        median_budget = np.nanmedian(self.data['Budget in USD'])
        self.data['Budget in USD'] = self.data['Budget in USD'].fillna(median_budget)
        return self.data

    def fill_missing_with_constant(self, constant_value="x"):
        """
        Fill NaN values in the DataFrame with a constant value.
        """
        self.data = self.data.replace(to_replace=np.nan, value=constant_value)
        return self.data

    def get_data(self):
        """
        Return the processed DataFrame.
        """
        return self.data

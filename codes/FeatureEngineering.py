import numpy as np
import pandas as pd
import re
from codes import DateManagement 

class FeatureEngineering:
    def __init__(self, file_path):
        """
        Initialize with the path to the CSV file.
        """
        self.data = pd.read_csv(file_path)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_colwidth', None)

    def date_into_columns(self):
        """
        Convert the 'Date' column to datetime and extract year, month, and day into separate columns.
        """
        self.data['Date'] = pd.to_datetime(self.data['Date'], format="%d/%m/%Y")
        self.data['Year'] = self.data['Date'].dt.year
        self.data['Month'] = self.data['Date'].dt.month
        self.data['Day'] = self.data['Date'].dt.day

    def awards_status(self, row):
        """
        Determine award status based on the number of awards.
        """
        return "Received" if int(row['Awards']) > 0 else "Didn't receive"

    def awards_status_generator(self):
        """
        Apply the awards_status method to generate a new column indicating award status.
        """
        self.data['Awards Rec / Not'] = self.data.apply(self.awards_status, axis=1)
        return self.data

    def time_since_release(self):
        """
        Calculate and add a column indicating the number of years since release.
        """
        """self.data['Date'] = pd.to_datetime(self.data['Date'])
        current_year = pd.Timestamp.now().year
        since_release = current_year - self.data['Date'].dt.year
        self.data['years_since_release'] = "Released " + since_release.astype(str) + " years ago" """
        self.data = DateManagement.DateManagement.time_since_release(self.data)
        return self.data
        


    def get_data(self):
        """
        Return the processed DataFrame.
        """
        return self.data

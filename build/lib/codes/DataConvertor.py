import numpy as np
import pandas as pd

class DataConvertor:
    def __init__(self, file_path):
        """
        Initialize with the path to the CSV file.
        """
        self.data = pd.read_csv(file_path)
        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)

    def convert_movie_id_to_ascii(self):
        """
        Convert non-numeric values in the "Movie Id" column to their ASCII representations.
        """
        self.data["Movie Id"] = self.data["Movie Id"].apply(
            lambda x: ''.join(str(ord(c)) for c in x) if not str(x).isnumeric() else x
        )
        return self.data

    def get_data(self):
        """
        Return the processed DataFrame.
        """
        return self.data

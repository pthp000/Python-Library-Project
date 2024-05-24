import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

class TextProcessor:
    def __init__(self, file_path):
        """
        Initialize with the path to the CSV file.
        """
        self.data = pd.read_csv(file_path)
        nltk.download('stopwords')  # Download NLTK stopwords
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_colwidth', None)

    def remove_stopwords(self, column_name):
        """
        Remove stopwords from the specified column.
        """
        stop = stopwords.words('english')
        self.data['Summary_without_stopwords'] = self.data[column_name].apply(lambda x: ' '.join([word for word in x.split() if word not in stop]))
        return self.data

    def convert_to_lowercase(self, column_name):
        """
        Convert text in the specified column to lowercase.
        """
        self.data['LowerCased_Result'] = self.data[column_name].apply(lambda x: x.lower())
        return self.data

    def remove_punctuation(self, column_name):
        """
        Remove punctuation from the specified column.
        """
        self.data['Removed Punctuation'] = self.data[column_name].apply(lambda x: re.sub(r'[^\w\s]+', '', x))
        return self.data

    def get_data(self):
        """
        Return the processed DataFrame.
        """
        return self.data

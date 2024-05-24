import pandas as pd

class DateManagement:
    @staticmethod
    def process_dates(data):
        """
        Convert 'Release Date' to datetime and extract year, month, and day.
        Drop the original 'Date' column.
        """
        data['Release Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
        data['Release Year'] = data['Release Date'].dt.year
        data['Release Month'] = data['Release Date'].dt.month
        data['Release Day'] = data['Release Date'].dt.day
        data = data.drop(columns=['Release Date'])
        return data
    
    @staticmethod
    def time_since_release(data):
        """
        Calculate and add a column indicating the number of years since release.
        """
        data['Date'] = pd.to_datetime(data['Date'])
        current_year = pd.Timestamp.now().year
        since_release = current_year - data['Date'].dt.year
        data['years_since_release'] = "Released " + since_release.astype(str) + " years ago"
        

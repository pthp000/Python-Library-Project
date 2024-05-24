
Term Project: Python Data Preprocessing Library (Publishable on PyPI) 
Course: Python Programming for Data Engineering
Done by : Asmaa Khourdaji - Amal Sabouni

Our project involves a series of classes designed to preprocess and handle different aspects of a dataset. The classes provide functionalities such as encoding categorical variables, processing dates, converting movie IDs, handling missing values and outliers, scaling numerical data, and processing text data.

Classes and Functionalities
1. CategoricalEncoder
This class handles the encoding of categorical variables and processing of dates.

Methods:
encode_categorical(): One-hot encodes categorical columns ('Genre', 'Shooting Location') and ensures all encoded columns are integers.

process_dates(): Processes dates using the DateManagement module.
get_data(): Returns the processed DataFrame.
2. DataConvertor
This class converts non-numeric movie IDs to their ASCII representations.

Methods:
convert_movie_id_to_ascii(): Converts non-numeric values in the "Movie Id" column to ASCII representations.
get_data(): Returns the processed DataFrame.
3. DateManagement
A utility class for handling date-related operations.

Methods:
process_dates(data): Converts 'Release Date' to datetime and extracts year, month, and day, then drops the original 'Date' column.
time_since_release(data): Calculates the number of years since the release and adds a corresponding column.
4. FeatureEngineering
This class focuses on feature engineering tasks.

Methods:
date_into_columns(): Extracts year, month, and day from the 'Date' column.
awards_status_generator(): Generates a new column indicating whether awards were received.
time_since_release(): Adds a column indicating the number of years since release using DateManagement.
get_data(): Returns the processed DataFrame.
5. MissingValueHandler
This class manages missing values in the dataset.

Methods:
check_missing_values(): Checks for missing values in the DataFrame.
fill_missing_with_mean(): Fills NaN values in 'Budget in USD' with the mean.
fill_missing_with_median(): Fills NaN values in 'Budget in USD' with the median.
fill_missing_with_constant(constant_value): Fills NaN values with a constant value.
get_data(): Returns the processed DataFrame.
6. OutlierHandler
This class identifies and corrects outliers in the dataset.

Methods:
identify_outliers(): Identifies outliers in 'Rating' and 'Budget in USD' using the IQR method.
correct_outliers(): Removes outliers from the dataset.
get_data(): Returns the processed DataFrame.
7. Scaler
This class standardizes and normalizes numerical data.

Methods:
standardize_data(): Standardizes 'Budget in USD' and 'Rating' using StandardScaler.
normalize_data(): Normalizes 'Budget in USD' and 'Rating' using MinMaxScaler.
get_data(): Returns the processed DataFrame.
8. TextProcessor
This class processes textual data.

Methods:
remove_stopwords(column_name): Removes stopwords from the specified column.
convert_to_lowercase(column_name): Converts text to lowercase in the specified column.
remove_punctuation(column_name): Removes punctuation from the specified column.
get_data(): Returns the processed DataFrame.
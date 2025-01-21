import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Drop rows with missing values
    numeric_columns = data.select_dtypes(include='number').columns
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
    

    # Drop duplicate rows
    data.drop_duplicates(inplace=True)

    return data

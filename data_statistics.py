import pandas as pd

def descriptive_statistics(data):
    if data.empty:
        print("The dataset is empty.")
    else:
        return data.describe()

def correlation_matrix(data):
    numeric_columns = data.select_dtypes(include='number')
    return numeric_columns.corr()

def detect_outliers(data, column_name):
    if column_name not in data.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the dataset.")
    
    data[column_name] = pd.to_numeric(data[column_name], errors='coerce')
    
    clean_data = data.dropna(subset=[column_name])
    
    Q1 = clean_data[column_name].quantile(0.25)
    Q3 = clean_data[column_name].quantile(0.75)
    
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = clean_data[(clean_data[column_name] < lower_bound) | (clean_data[column_name] > upper_bound)]
    
    return outliers

def display_frequency_distribution(data, column_name):
    if column_name not in data.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the dataset.")
    
    frequency_distribution = data[column_name].value_counts().sort_index()

    return frequency_distribution
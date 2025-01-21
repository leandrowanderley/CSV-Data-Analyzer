import pandas as pd

def descriptive_statistics(data):
    # Calculate summary statistics
    return data.describe()

def correlation_matrix(data):
    # Calculate correlation matrix
    numeric_columns = data.select_dtypes(include='number')
    return numeric_columns.corr()
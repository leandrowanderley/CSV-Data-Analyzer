
import pandas as pd

file_path = 'cars.csv'
data = pd.read_csv(file_path)

print(data.columns)
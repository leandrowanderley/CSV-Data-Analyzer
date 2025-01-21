
import pandas as pd

def descriptive_statistics(data):
    if data.empty:
        print("The dataset is empty.")
    else:
        return data.describe()

file_path = 'cars.csv'
data = pd.read_csv(file_path)

x = int(input())
match x:
    case 1:    
        print(descriptive_statistics(data))
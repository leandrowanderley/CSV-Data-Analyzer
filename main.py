from dataprocessing import load_data, clean_data
from data_statistics import descriptive_statistics, correlation_matrix
from visualization import plot_histogram, plot_correlation_heatmap

file_path = 'cars.csv'
data = load_data(file_path)
data = clean_data(data)

print("Descriptive statistics:")
print(descriptive_statistics(data))

print("\nCorrelation matrix:")
print(correlation_matrix(data))

plot_histogram(data, 'hp')
plot_correlation_heatmap(data)


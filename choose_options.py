# from dataprocessing import load_data, clean_data
from data_statistics import *
from visualization import *
def select_option(data, option):
    match option:
        # Problem in the next line
        case 1:
            print("Descriptive statistics:")
            statistics = descriptive_statistics(data)
            if statistics is not None:
                print(statistics)
            else:
                print("The dataset is empty.")
        case 2:
            print("Correlation matrix:")
            print(correlation_matrix(data))
        case 3:
            print("Detecting outliers:")
            column_name = input("Enter the column name to detect outliers: ")
            print(detect_outliers(data, column_name))
        case 4:
            print("Displaying frequency distribution:")
            column_name = input("Enter the column name to display frequency distribution: ")
            print(display_frequency_distribution(data, column_name))
        case 5:
            print("Plotting histogram:")
            column_name = input("Enter the column name to plot histogram: ")
            plot_histogram(data, column_name)
        case 6:
            print("Plotting correlation heatmap:")
            plot_correlation_heatmap(data)
        case 7:
            print("Generating boxplot:")
            column_name = input("Enter the column name to generate boxplot: ")
            generate_boxplot(data, column_name)
        case 8:
            print("Generating scatter plot:")
            x_column = input("Enter the x-axis column name: ")
            y_column = input("Enter the y-axis column name: ")
            generate_scatter_plot(data, x_column, y_column)
        case 9:
            print("Generating pie chart:")
            column_name = input("Enter the column name to generate pie chart: ")
            generate_pie_chart(data, column_name)
        case 10:
            print("Filtering data:")
            # Add your implementation for data filtering
        case 11:
            print("Sorting data:")
            # Add your implementation for data sorting
        case 12:
            print("Normalizing column:")
            # Add your implementation for column normalization
        case 13:
            print("Converting units:")
            # Add your implementation for unit conversion
        case 14:
            print("Handling missing values:")
            # Add your implementation for handling missing values
        case 15:
            print("Adding a new column:")
            # Add your implementation for adding a new column
        case 16:
            print("Grouping and aggregating data:")
            # Add your implementation for grouping and aggregation
        case 17:
            print("Highlighting high correlations:")
            # Add your implementation for highlighting high correlations
        case 18:
            print("Exporting cleaned data:")
            # Add your implementation for exporting cleaned data
        case 19:
            print("Generating summary report:")
            # Add your implementation for generating a summary report
        case 20:
            print("Comparing columns:")
            # Add your implementation for comparing columns
        case 21:
            print("Generating trend analysis:")
            # Add your implementation for trend analysis
        case 22:
            print("Predicting next value:")
            # Add your implementation for predicting the next value
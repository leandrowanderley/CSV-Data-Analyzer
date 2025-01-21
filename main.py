from dataprocessing import load_data, clean_data
from choose_options import select_option

print("Hello, welcome to dataset analysis!\n")
print("This program will load a dataset that you choose and perform some basic analysis on it.\n")
while True:
    file_path = input("Did you put the dataset in the same folder as this program?\nIf not, please do so and enter the name of the dataset file here: ")
    file_path = file_path.lower()
    file_path = file_path.replace(" ", "_")
    if file_path == None or file_path == "":
        print("Please enter a valid file name.")
        continue
    break

if file_path.endswith(".csv") == False:
    file_path += ".csv"
print("Loading dataset...")
try:
    data = load_data(file_path)
    data = clean_data(data)
except Exception as e:
    print(f"An error occurred loading data: {e}\nProgram will now exit.")
    exit(1)

print("What you want to do with the dataset?\n")

print("\nOptions:")
print("1. Display descriptive statistics")
print("2. Display correlation matrix")
print("3. Detect outliers in a column")
print("4. Display frequency distribution of a column")
print("5. Plot a histogram of a column")
print("6. Plot a correlation heatmap")
print("7. Generate a boxplot for a column")
print("8. Generate a scatter plot between two columns")
print("9. Generate a pie chart for a column")
print("10. Filter data based on a condition")
print("11. Sort data by a column")
print("12. Normalize a column")
print("13. Convert units in a column")
print("14. Handle missing values in the dataset")
print("15. Add a new column to the dataset")
print("16. Group and aggregate data")
print("17. Highlight high correlations in the dataset")
print("18. Export cleaned data to a CSV file")
print("19. Generate a summary report of the data")
print("20. Compare two columns")
print("21. Generate trend analysis")
print("22. Predict the next value in a column")
print("23. Exit the program")

option = 0
while True:
    try:
        option = int(input("\nWhat do you want to do with the dataset? Enter a number (1-23): "))
        actions = {
            # data_statistics
            1: "descriptive_statistics(data)",
            2: "correlation_matrix(data)",
            3: "detect_outliers(data, 'column_name')",
            4: "display_frequency_distribution(data, 'column_name')",

            # visualization
            5: "plot_histogram(data, 'column_name')",
            6: "plot_correlation_heatmap(data)",
            7: "generate_boxplot(data, 'column_name')",
            8: "generate_scatter_plot(data, 'x_column', 'y_column')",
            9: "generate_pie_chart(data, 'column_name')",

            # Data Cleaning and Transformation
            10: "filter_data(data, 'your_condition')",
            11: "sort_data(data, 'column_name', ascending=True)",
            12: "normalize_column(data, 'column_name')",
            13: "convert_units(data, 'column_name', 'conversion_factor')",
            14: "handle_missing_values(data, 'strategy')",
            15: "add_new_column(data, 'new_column_name', 'calculation')",

            # Grouping and Aggregation
            16: "group_and_aggregate(data, 'group_column', 'agg_column', 'agg_function')",
            17: "highlight_high_correlations(data, threshold=0.8)",

            # Reporting and Exporting
            18: "export_cleaned_data(data, 'output_file.csv')",
            19: "generate_summary_report(data)",

            # Advanced Analysis and Predictions
            20: "compare_columns(data, 'column1', 'column2')",
            21: "generate_trend_analysis(data, 'time_column', 'value_column')",
            22: "predict_next_value(data, 'column_name')",

            # Exit
            23: "exit(0)"
        }

        if option in actions:
            # Placeholder for executing the action
            print(f"Performing action: {actions[option]}\n\n")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if option == 23:
    print("Thank you for using the program.")
    exit(0)
select_option(option, data)

print("\n\n")

print("Thank you for using the program.\n")







# print("CurrentData:")

# print("Descriptive statistics:")
# print(descriptive_statistics(data))

# print("\nCorrelation matrix:")
# print(correlation_matrix(data))

# plot_histogram(data, 'hp')
# plot_correlation_heatmap(data)


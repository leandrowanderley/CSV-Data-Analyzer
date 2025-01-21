# CSV Data Analyzer

A Python project for analyzing and visualizing data from CSV files. This tool loads, cleans, analyzes, and visualizes data, making it easier to derive insights from large datasets. It uses libraries such as Pandas, Seaborn, and Matplotlib for data processing and visualization.

## Features

- **Data Import**: Load CSV data into a Pandas DataFrame.
- **Data Cleaning**: Handle missing values and data type issues.
- **Statistical Analysis**: Generate descriptive statistics and correlation matrices.
- **Visualization**: Plot histograms and other data visualizations.

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.6 or higher
- Pandas
- Seaborn
- Matplotlib

You can install the required libraries using `pip`:

```bash
pip install pandas seaborn matplotlib
```

## How to Use

1. Clone this repository:
```bash
git clone https://github.com/your-username/CSV-Data-Analyzer.git
```

2. Navigate to the project directory:
```bash
cd CSV-Data-Analyzer
````

3. Place your CSV file in the project directory.
4. Modify the `file_path` variable in `main.py` to point to your CSV file.
5. Run the script:

```bash
python main.py
```

### Example Output:

The script will display:
- Descriptive statistics (mean, median, standard deviation, etc.)
- A correlation matrix for the numerical columns.
- A histogram of a selected column.
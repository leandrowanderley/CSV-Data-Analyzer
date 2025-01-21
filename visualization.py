import seaborn
import matplotlib.pyplot as plot

def plot_histogram(data, column):
    seaborn.histplot(data[column], kde=True)
    plot.title(f'Histograma de {column}')
    plot.show()

def plot_correlation_heatmap(data):
    correlation = data.corr()
    seaborn.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
    plot.title('Mapa de calor da matriz de correlação')
    plot.show()

def generate_boxplot(data, column_name):
    if column_name not in data.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the dataset.")
    
    plot.figure(figsize=(8, 6))
    seaborn.boxplot(data=data, x=column_name)
    plot.title(f"Boxplot of {column_name}")
    plot.xlabel(column_name)
    plot.show()

def generate_scatter_plot(data, x_column, y_column):
    if x_column not in data.columns or y_column not in data.columns:
        raise ValueError(f"One or both columns '{x_column}' and '{y_column}' do not exist in the dataset.")
    
    plot.figure(figsize=(8, 6))
    plot.scatter(data[x_column], data[y_column], c='blue', edgecolors='k', alpha=0.7)
    plot.title(f"Scatter Plot: {x_column} vs {y_column}")
    plot.xlabel(x_column)
    plot.ylabel(y_column)
    plot.grid(True)
    plot.show()

def generate_pie_chart(data, column_name):
    if column_name not in data.columns:
        raise ValueError(f"The column '{column_name}' does not exist in the dataset.")
    
    value_counts = data[column_name].value_counts()

    plot.figure(figsize=(8, 8))
    plot.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140, colors=plot.cm.Paired.colors)
    plot.title(f"Pie Chart: Distribution of {column_name}")
    plot.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plot.show()
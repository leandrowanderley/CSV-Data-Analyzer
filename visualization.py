import seaborn
import matplotlib.pyplot as plot

def plot_histogram(data, column):
    # Plota um histograma de uma coluna específica.
    seaborn.histplot(data[column], kde=True)
    plot.title(f'Histograma de {column}')
    plot.show()

def plot_correlation_heatmap(data):
    # Plota um mapa de calor da matriz de correlação.
    correlation = data.corr()
    seaborn.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
    plot.title('Mapa de calor da matriz de correlação')
    plot.show()
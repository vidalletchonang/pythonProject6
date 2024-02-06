import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leggi il dataset
dataset = pd.read_csv(r'C:\Users\vidal\PycharmProjects\pythonProject6\dataset_climatico.csv')

# Seleziona solo le colonne di interesse per l'analisi di correlazione
columns_of_interest = ['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']

# Crea un sotto-dataset con le colonne di interesse
subset_dataset = dataset[columns_of_interest]

# Calcola la matrice di correlazione
correlation_matrix = subset_dataset.corr()

# Crea una heatmap per visualizzare la correlazione
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matrice di Correlazione tra Variabili Meteorologiche')
plt.show()

# Statistiche descrittive
desc_stats = subset_dataset.describe()

# Creazione di un report
report = pd.DataFrame({
    'Media': desc_stats.loc['mean'],
    'Mediana': subset_dataset.median(),
    'Deviazione Standard': desc_stats.loc['std'],
    'Primo Quartile': desc_stats.loc['25%'],
    'Terzo Quartile': desc_stats.loc['75%'],
})

# Aggiungi l'indice del dataset come colonna
report['Stazione Meteorologica'] = dataset['stazione_meteorologica']

# Setta l'indice
report.set_index('Stazione Meteorologica', inplace=True)

# Stampa il report
print(report)

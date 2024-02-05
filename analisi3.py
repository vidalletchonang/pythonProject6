import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Leggi il dataset
dataset = pd.read_csv(r'C:\Users\vidal\PycharmProjects\pythonProject6\dataset_climatico.csv')

# 1. Pulizia dei dati (se necessario, verifica la presenza di valori mancanti)
dataset_cleaned = dataset.dropna()

# 2. Normalizzazione dei dati
columns_to_normalize = ['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']
scaler = StandardScaler()
dataset_cleaned[columns_to_normalize] = scaler.fit_transform(dataset_cleaned[columns_to_normalize])

# 3. Analisi Esplorativa dei Dati
# Calcolare statistiche descrittive
desc_stats = dataset_cleaned[columns_to_normalize].describe()

# Creare grafici
for column in columns_to_normalize:
    plt.figure(figsize=(8, 6))
    sns.histplot(dataset_cleaned[column], kde=True)
    plt.title(f'Distribuzione di {column}')
    plt.xlabel(column)
    plt.ylabel('Frequenza')
    plt.show()

# Analisi di Correlazione con Heatmap
corr_matrix = dataset_cleaned[columns_to_normalize].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matrice di Correlazione')
plt.show()

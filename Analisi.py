import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Leggi il dataset
dataset = pd.read_csv(r'C:\Users\vidal\PycharmProjects\pythonProject6\dataset_climatico.csv')

# Pulizia dei dati (se necessario, verifica la presenza di valori mancanti)
dataset_cleaned = dataset.dropna()

# Normalizzazione dei dati
columns_to_normalize = ['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']
scaler = StandardScaler()
dataset_cleaned[columns_to_normalize] = scaler.fit_transform(dataset_cleaned[columns_to_normalize])

# Converti la colonna 'data_osservazione' in formato datetime
dataset_cleaned['data_osservazione'] = pd.to_datetime(dataset_cleaned['data_osservazione'])

# Imposta la colonna 'data_osservazione' come indice
dataset_cleaned = dataset_cleaned.set_index('data_osservazione')

# Raggruppa per mese e calcola la temperatura media
monthly_avg_temp = dataset_cleaned.resample('M')['temperatura_media'].mean()

# Visualizza il risultato
plt.figure(figsize=(10, 6))
monthly_avg_temp.plot(kind='bar', color='skyblue')
plt.title('Temperatura Media Mensile')
plt.xlabel('Mese')
plt.ylabel('Temperatura Media')
plt.show()


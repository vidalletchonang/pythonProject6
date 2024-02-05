import pandas as pd
from sklearn.preprocessing import StandardScaler

# Leggi il dataset
dataset = pd.read_csv(r'C:\Users\vidal\PycharmProjects\pythonProject6\dataset_climatico.csv')


# Seleziona solo le colonne da normalizzare
columns_to_normalize = ['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']

# Inizializza lo scaler
scaler = StandardScaler()

# Applica la normalizzazione Z-score solo alle colonne selezionate
dataset[columns_to_normalize] = scaler.fit_transform(dataset[columns_to_normalize])

# Stampa il dataset normalizzato
print(dataset)

import pandas as pd

# Lee el archivo csv
df = pd.read_csv('Olas_45000.csv', delimiter="\t")

# Selecciona solo la columna 'en_ente_mis'
df_ente_mis = df[['en_ente_mis']]

#df_ente_mis= df[ df['en_nombre'].str.contains("GHISLAINE")]

print(df.columns)

# Guarda el resultado en un nuevo archivo csv
df_ente_mis.to_csv('olas_09_08_23.csv', index=False)

print("Archivo convertido exitosamente!")
import pandas as pd
import re
import csv

def remove_quotes(row):
    new_value= re.sub("[\"']","",str(row)).strip().upper()
    return new_value

df = pd.read_csv('jess.csv', delimiter=",", quotechar="'")

filtrado = df[['Nombre Completo','Entidad o dependencia']]

new_filtrado= filtrado.applymap(lambda row: remove_quotes(row=row))
#print(new_filtrado)

new_filtrado_sorted=new_filtrado.sort_values(by='Entidad o dependencia', ascending=True)

print(new_filtrado_sorted)

#print(filtrado)

new_filtrado_sorted.to_csv('jess_procesado.csv', index=False, sep=';', quoting=csv.QUOTE_NONE, )

print("Archivo convertido exitosamente!")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("support_uke_24.xlsx")  # Leser excel filen

u_dag = df.iloc[:, 0].to_numpy()  # Kolonne 1 med navn u_dag. Dette ta med alle verdiene fra denne kolonnen
kl_slett = df.iloc[:, 1].to_numpy()  # Kolonne 2, dette tar med alle verdiene inne i variabelen.
varighet = df.iloc[:, 2].to_numpy() 
score = df.iloc[:, 3].to_numpy() 

# print(u_dag)
# print(kl_slett)  
# print(varighet) 
# print(score)  # Skriver ut score

ukedager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]  # Liste over ukedagene 
antall_per_dag = pd.Series(u_dag).value_counts().reindex(ukedager, fill_value=0)  # Teller antall henvendelser per dag

plt.figure(figsize=(8, 5))  # Lager en figur
plt.bar(antall_per_dag.index, antall_per_dag.values)  # Lager stolpediagram av antall per dag
plt.title("Antall henvendelser per ukedag")  # Tittel på diagrammet
plt.xlabel("Ukedag")  # Navn på x-aksen
plt.ylabel("Antall henvendelser")  # Navn på y-aksen
plt.tight_layout()  # Justerer layout
plt.show()  # Viser diagrammet
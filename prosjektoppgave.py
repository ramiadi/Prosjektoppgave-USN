import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("support_uke_24.xlsx")  # Leser excel filen

u_dag = df.iloc[:, 0].to_numpy()  # Kolonne 1 med navn u_dag. Dette ta med alle verdiene fra denne kolonnen
kl_slett = df.iloc[:, 1].to_numpy()  # Kolonne 2, dette tar med alle verdiene inne i variabelen.
varighet = df.iloc[:, 2].to_numpy() 
score = df.iloc[:, 3].to_numpy() 

print(u_dag)
print(kl_slett)  
print(varighet) 
print(score)  
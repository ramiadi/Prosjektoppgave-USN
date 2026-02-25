import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("support_uke_24.xlsx")  # Leser excel filen

#Oppgave del a)
u_dag = df.iloc[:, 0].to_numpy()  # Kolonne 1 med navn u_dag. Dette ta med alle verdiene fra denne kolonnen
kl_slett = df.iloc[:, 1].to_numpy()  # Kolonne 2, dette tar med alle verdiene inne i variabelen.
varighet = pd.to_timedelta(df.iloc[:, 2]).dt.total_seconds().to_numpy() # Kolonne 3, tar med alle verdier inne i variabelen men konverterer dette til sekunder istedet for klokkeslett.
score = df.iloc[:, 3].to_numpy() 

# print(u_dag)
# print(kl_slett)  
# print(varighet) 
# print(score)  # Skriver ut score

#Oppgave del b
ukedager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]  # Liste over ukedagene 
antall_per_dag = pd.Series(u_dag).value_counts().reindex(ukedager, fill_value=0)  # Teller antall henvendelser per dag

plt.figure(figsize=(8, 5))  # Lager en figur
plt.bar(antall_per_dag.index, antall_per_dag.values)  # Lager stolpediagram av antall per dag
plt.title("Antall henvendelser per ukedag")  # Tittel på diagrammet
plt.xlabel("Ukedag")  # Navn på x-aksen
plt.ylabel("Antall henvendelser")  # Navn på y-aksen
plt.tight_layout()  # Justerer layout
plt.show()  # Viser diagrammet

# Oppgave del c)
minste_varighet = varighet[0] # Lagrer en variabel for å sjekke ut verdi senere i if testen
lengste_varighet = varighet[0]
summer_varighet = 0

print("Varigheter loggført i uke 24:")
for tid in varighet: # For løkke for å gå gjennom alle verdier innefor kolonne varighet. Så lenge if testene blir gyldige, skal en av varighetene oppdateres
	summer_varighet += tid # dette er for å summere alle verdiene fra varighet, slik at jeg kan finne gjennomsnittet senere
	if tid < minste_varighet: # hvis tid(verdien) er mindre enn varigheten, har programmet funnet en enda mindre varighet
		minste_varighet = tid # Oppdater minste varighet
	if tid > lengste_varighet: #Igjen hvis tid(verdien) er større enn varigheten, har programmet funnet en enda større varighet.
		lengste_varighet = tid # Oppdater største varighet	
	#Neste løkke, eventuelt stopp løkke hvis if testene ikke lenger er oppfylt

print(f"Korteste samtaletid i uke 24 er i sekunder: {minste_varighet}")
print(f"Lengste samtaletid i uke 24 er i sekunder: {lengste_varighet}")

gjennomsnitt = (summer_varighet / len(varighet)) # Har funnet summen av alle varighetene og deler det på lengden av varighet. Når det er gjort, har jeg funnet gjennomsnittet.
print(f"Gjennomsnittlig samtaletid i uke 24 er i sekunder: {gjennomsnitt}")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("support_uke_24.xlsx")  # Leser excel filen

#Oppgave del a)
u_dag = df.iloc[:, 0].to_numpy()  # Kolonne 1 med navn u_dag. Dette ta med alle verdiene fra denne kolonnen
kl_slett = pd.to_datetime(df.iloc[:, 1], format="%H:%M:%S").dt.hour  # Kolonne 2, dette tar med alle verdiene inne i variabelen.
varighet = pd.to_timedelta(df.iloc[:, 2]).dt.total_seconds().to_numpy() # Kolonne 3, tar med alle verdier inne i variabelen, men konverterer dette til sekunder istedet for klokkeslett.
tilfredshet = df.iloc[:, 3].to_numpy() 

# print(u_dag)
# print(kl_slett)  
# print(varighet) 
# print(score)  # Skriver ut score

#Oppgave del b
def finn_antall_henvendelser():
    ukedager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]  # Liste over ukedagene 
    antall_per_dag = pd.Series(u_dag).value_counts().reindex(ukedager, fill_value=0)  # Teller antall henvendelser per dag

    plt.figure(figsize=(8, 5))  # Lager en figur
    plt.bar(antall_per_dag.index, antall_per_dag.values)  # Lager stolpediagram av antall per dag
    plt.title("Antall henvendelser per ukedag")  # Tittel på diagrammet
    plt.xlabel("Ukedag")  # Navn på x-aksen
    plt.ylabel("Antall henvendelser")  # Navn på y-aksen
    plt.tight_layout()  # Justerer layout
    plt.show()  # Viser diagrammet
finn_antall_henvendelser()

# Oppgave del c)
def finn_gjennomsnitt_minst_og_lengst_varighet(varigheter):
    minste_varighet = varigheter[0] # Lagrer en variabel for å sjekke ut verdi senere i if testen
    lengste_varighet = varigheter[0]
    summer_varighet = 0 # Dette er for å summerer alle varighetene i en variabel

    print("Varigheter loggført i uke 24:")
    for tid in varigheter: # For løkke for å gå gjennom alle verdier innefor kolonne varighet. Så lenge if testene blir gyldige, skal en av varighetene oppdateres
        summer_varighet += tid # dette er for å summere alle verdiene fra varighet, slik at jeg kan finne gjennomsnittet senere
        if tid < minste_varighet: # hvis tid(verdien) er mindre enn varigheten, har programmet funnet en enda mindre varighet
            minste_varighet = tid # Oppdater minste varighet
        if tid > lengste_varighet: #Igjen hvis tid(verdien) er større enn varigheten, har programmet funnet en enda større varighet.
            lengste_varighet = tid # Oppdater største varighet	
        #Neste løkke, eventuelt stopp løkke hvis if testene ikke lenger er oppfylt

    print()
    print(f"Korteste samtaletid i uke 24 er i sekunder: {minste_varighet}")
    print(f"Lengste samtaletid i uke 24 er i sekunder: {lengste_varighet}")

    gjennomsnitt = (summer_varighet / len(varigheter)) # Har funnet summen av alle varighetene og deler det på lengden av varighet. Når det er gjort, har jeg funnet gjennomsnittet.
    print(f"Gjennomsnittlig samtaletid i uke 24 er i sekunder: {gjennomsnitt}")
finn_gjennomsnitt_minst_og_lengst_varighet(varighet)

#Oppgave del e)
def total_antall_henvendelser_tidsrom(kl_sletter):
    bolker = { # lager bolker for å definere tidsrom ved å bruke dictionary
        "08-10": 0, # startverdi er 0, altså ikke noe
        "10-12": 0,
        "12-14": 0,
        "14-16": 0
    } # Strengene (altså klokkeslettene) er .keys(), og startverdiene (feks: 0) er .values(). Vi skal bruke disse senere.

    for time in kl_sletter:
        if 8 <= time < 10: # hvis timen er større eller lik time og samtidig mindre enn 10, skal det økes med 1
            bolker["08-10"] += 1 #hvis betingelsen over er oppfylt, øk verdien med 1
        elif 10 <= time < 12: # samme med de andre if testene
            bolker["10-12"] += 1
        elif 12 <= time < 14:
            bolker["12-14"]
        elif 14 <= time <16:
            bolker["14-16"] += 1
        else: # tok med i tilfelle der noe er utenfor
            print(f"Klokkeslett {time} er utenfor støttet tidsrom")

    print()
    print("Antall henvendelser per tidsrom i uke 24:") 
    for bolk, antall in bolker.items(): #siden vi bruker dictionary, skriver vi inn .items() for å hente verdier
        print(f"Kl {bolk}: {antall} henvendelser")

    plt.figure(figsize=(7, 7)) 
    plt.pie(bolker.values(), labels=bolker.keys(), autopct="%1.1f%%") # Lager kakediagram, .values() henter verdiene og .keys() henter klokkeslett strengene fra bolker dictionary.
    plt.title("Henvendelser per tidsrom i uke 24")
    plt.tight_layout()
    plt.show() # vis
total_antall_henvendelser_tidsrom(kl_slett)

#Oppgave del f)
def finn_kundens_tilfredshet(score):
    score_utenNaN = score[~np.isnan(score)] #Henter verdier fra kolonnen som ikke er NaN
    antall_totalt = len(score_utenNaN) #Finner lengden av faktiske verdier
    antall_positive = 0
    antall_nøytrale = 0
    antall_negative = 0
    for s in score_utenNaN: # for løkke som går gjennom faktiske verdier
        if s >= 9: # er verdien større eller lik 9? betingelse oppfylt
            antall_positive += 1 # øk positivitet med 1
        elif s >= 7: # Dersom s ikke er større enn eller lik tallet 9, sjekk om at den er større eller lik tallet 7
            antall_nøytrale += 1 # Kundens tilfredshet er nøytral, øk dette med 1
        else: # Hvis ingen av if testene over har blitt oppfylt, regnes dette som negativ tilfredshet fra kunden
            antall_negative += 1 # Øk negativ tilfredshet fra kunden med 1 

    prosent_positive = (antall_positive / antall_totalt) * 100 # for å finne i prosentvis, må mån finne antall positive og dele med lengden av faktiske verdier, deretter gange med 100
    prosent_nøytrale = (antall_nøytrale / antall_totalt) * 100
    prosent_negative = (antall_negative / antall_totalt) * 100
    NPS = prosent_positive - prosent_negative # For å finne NPS, må vi subtrahere positiv og negativ.

    print()
    print(f"Antall respondenter: {antall_totalt}")
    print(f"Positive (9-10): {antall_positive} ({prosent_positive:.1f}%)")
    print(f"Nøytrale (7-8): {antall_nøytrale} ({prosent_nøytrale:.1f}%)")
    print(f"Negative (1-6): {antall_negative} ({prosent_negative:.1f}%)")
    print(f"NPS for supportavdelingen i uke 24: {NPS:.1f}")
finn_kundens_tilfredshet(tilfredshet) # Kaller opp funksjonen
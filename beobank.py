import pandas as pd

mcHuidig = pd.read_excel('Overzicht.xlsx', sheet_name ='Volgende uittreksel', skiprows=6)
mcVorig = pd.read_excel('Overzicht.xlsx', sheet_name ='Vorige uittreksels', skiprows=3)

alles = [mcHuidig, mcVorig]

mcAlles = pd.concat(alles)



ynabGegevens=mcAlles[['Datum', 'Omschrijving', 'Omschrijving', 'Bedrag']]

#Hernoem de kolommen naar de door Ynab gebruikte naam
ynabGegevens.columns = ['Date', 'Payee', 'Memo', 'Amount']

ynabGegevens.to_csv('ynabBeo.csv', index=False)

#! /usr/bin/python
# script om Argenta-excel's met verrichtingen om te vormen naar een CSV voor YNAB

import pandas as pd
import os

# vind de excel met de gegevens van Argenta in - onafhankelijk van je reknr en datum
files = os.listdir(os.curdir)
for file in files:
    if file.startswith('Argenta_BE'):
        gegevens = file

# lees de gevonden file in
bankGegevens = pd.read_excel(gegevens)

# Haal er alleen de relevante gegevens voor YNAB uit
ynabGegevens = bankGegevens[['Valutadatum', 'Naam tegenpartij', 'Mededeling', 'Bedrag']]

#Hernoem de kolommen naar de door Ynab gebruikte naam
ynabGegevens.columns = ['Date', 'Payee', 'Memo', 'Amount']

#Exporteer de csv
ynabGegevens.to_csv('ynabArgenta.csv', index=False)

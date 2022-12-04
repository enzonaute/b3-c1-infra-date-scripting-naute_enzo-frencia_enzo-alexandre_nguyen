#!/usr/bin/python3

import csv
# on définie les fichier csv dans des variables

FichierL = 'conso-annuelles_v1.csv'
FichierE = 'conso-clean.csv'

# on définie le premeir csv soit en mode lecture, et le deuxième soit en mode écriture

with open(FichierL, 'r', newline='', encoding='latin-1') as inputFile, open(FichierE, 'w') as writerFile:
    delete = csv.reader(inputFile, delimiter=';')
    write = csv.writer(writerFile, delimiter=';')
    # création d'une fonction qui vas faire la supression des espaces vides et additionné les conso ann 1 et conso ann 2

    def Clean_File(test):
        list = []
        tab = test
        equip, id, conso1, conso2, type = tab
        tab[2] = conso1.replace(",", ".")
        tab[3] = conso2.replace(",", ".")
        if equip == '':
            del test
        elif id == '':
            del test
        elif conso1 == '':
            del test
        elif conso2 == '':
            del test
        elif type == '':
            del test
        elif equip == 'Appareil suivi':
            del test
        elif conso2 == '-':
            del test
        else:
            total = float(tab[2]) + float(tab[3])
            total = int(total)
            del tab[2]
            del tab[2]
            del tab[2]
            tab.append(total)
            tab.append(type)
            write.writerow(tab)
    # Parcours chaque ligne du csv
    for ligne in delete:
        Clean_File(ligne)

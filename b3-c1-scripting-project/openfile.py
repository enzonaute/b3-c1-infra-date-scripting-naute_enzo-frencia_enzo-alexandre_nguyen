import csv 
with open('conso-annuelles_v1.csv','r', encoding ='latin-1') as open:
	file = csv.DictReader(open,delimiter=';')
	tab=[]

	for ligne in file:
		print (dict(ligne))
		tab.append(ligne)
	print (len(tab))
	long = len(tab)
	i = 0
	while i < long:
		longueur = len(tab[i])
		i = i + 1
	print ("il y a "+str(long)+" lignes avec "+str(longueur)+ " données.")

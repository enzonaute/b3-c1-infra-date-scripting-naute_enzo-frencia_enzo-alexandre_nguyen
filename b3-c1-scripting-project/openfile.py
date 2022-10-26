import csv 

in_path = 'conso-annuelles_v1.csv'
out_path = 'clean-conso.csv'


with open(in_path, encoding ='latin-1') as open:
	file = csv.DictReader(open,delimiter=';')
	tab=[]

	for ligne in file:
		print (dict(ligne))
		tab.append(ligne)

	long = len(tab)
	i = 0
	while i < long:
		longueur = len(tab[i])
		print (tab[i])
		i = i + 1
	print ("il y a "+str(long)+" lignes avec "+str(longueur)+ " données.")
	with open(out_path) as clean:
		clean.write('nonoon')	



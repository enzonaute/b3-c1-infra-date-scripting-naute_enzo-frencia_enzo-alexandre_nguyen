import csv

in_path = 'conso-annuelles_v1.csv'
out_path = 'clean-conso.csv'

with open(in_path, 'r', newline='',encoding='latin-1') as inputFile, open(out_path, 'w') as writerFile:
	read_file = csv.reader(inputFile)
	for ligne in inputFile:
		writerFile.write(ligne)




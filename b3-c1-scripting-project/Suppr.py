import csv
with open('clean-conso.csv') as suppr, open('super_clean_conso.csv','w') as clean:
	delete = csv.reader(suppr, delimiter=';')
	write = csv.writer(clean, delimiter =';')
	i = 0
	tab = []
	global row
	def Tri_File(test):
		tab = test
		equip,id,conso1,conso2,type = tab
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
		else:
			write.writerow(test)
	for row in delete:
		Tri_File(row)


# import csv

# with open('conso-annuelles_v1.csv', encoding="latin-1") as csvfile:
#     csvreader = csv.reader(csvfile)

#     # data=list(csvreader)

# csvreader=[x for x in csvreader if '' not in x and '0' not in x]

# csvfile.write(csvreader) 


import csv
import re

with open('conso-annuelles_v1.csv', encoding="latin-1" ) as csv_file:
    reader = csv.reader(csv_file)
    result = [[items for items in row if items != '' and items == re.sub('','',items)] for row in reader]

    print(re.sub("[,]", ".", csv_file))
print(result)


# def no_blank(fd):
#     try:
#         while True:
#             line = next(fd)
#             if len(line.strip()) != 0:
#                 yield line
#     except:
#         return
# #Read the CSV file.
# with open('conso-annuelles_v1.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(no_blank(csv_file))


# import pandas as pd         

# df = pd.read_csv("conso-annuelles_v1.csv", on_bad_lines='skip', encoding="latin-1", sep=',').dropna()
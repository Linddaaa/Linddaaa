# import csv

# with open('fails.csv', mode ='r')as file:     #atver csv failu
#     csv_reader = csv.reader(file, delimiter=',')    #izveido csv lasītāja objektu
#     for ieraksts in csv_reader:     #ciklā nolasa visus ierakstus
#         Vards = ieraksts[0]         #atlasa tikai vārda un nodarbošanās laukus
#         Nodarbosanas = ieraksts[3]
#         print(f"{Vards}-{Nodarbosanas}")    #izdrukā ierakstu

# file.close()    #aizver csv failu         


import pandas

csvFiles = pandas.read_csv('fails.csv')
print(csvFiles)
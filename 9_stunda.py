# import csv

# with open('fails.csv', mode ='r')as file:     #atver csv failu
#     csv_reader = csv.reader(file, delimiter=',')    #izveido csv lasītāja objektu
#     for ieraksts in csv_reader:     #ciklā nolasa visus ierakstus
#         Vards = ieraksts[0]         #atlasa tikai vārda un nodarbošanās laukus
#         Nodarbosanas = ieraksts[3]
#         print(f"{Vards}-{Nodarbosanas}")    #izdrukā ierakstu

# file.close()    #aizver csv failu         


# import pandas

# csvFiles = pandas.read_csv('fails.csv')
# print(csvFiles)


# import json
# with open('example_2.json', 'r') as f:
#     data = json.load(f)
#     for i in data['quiz']:
#         print(i)
# f.close()

import json
arhivs = open(dati.json", "w")
json.dump(dati,arhivs, indent=4)
arhivs.close()
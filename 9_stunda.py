import csv

with open('fails.csv', mode ='r')as file:     #atver csv failu
    csv_reader = csv.reader(file, delimiter=',')    #izveido csv lasītāja objektu
    for ieraksts in csv_reader:     #ciklā nolasa visus ierakstus
        Vārds = ieraksts[0]         #atlasa tikai vārda un nodarbošanās laukus
        Nodarbošanās = ieraksts[3]
        print(f"{Vārds}-{Nodarbošanās}")    #izdrukā ierakstu

file.close()    #aizver csv failu         
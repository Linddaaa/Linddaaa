import csv
 
with open('liepaja_atskaite.cv', mode ='r') as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines)
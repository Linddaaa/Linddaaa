import csv
import random

with open('random_numbers.csv', 'w', newline="") as f:
          writer = csv.writer(f)
          writer.writerow(['Random numbers'])
          for i in range(50):
                random_number = random.randint(0, 1000)
                writer.writerow([random_number])

f.close()
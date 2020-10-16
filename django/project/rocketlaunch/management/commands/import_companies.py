# TODO Django management command to import companies

import csv
with open('/tmp/csv/rocket_companies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

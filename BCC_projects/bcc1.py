import csv
import sys

if len(sys.argv) != 3:
    print("Usage: python *.csv")
    print(sys.argv)
    sys.exit(1)

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
print(reader) 




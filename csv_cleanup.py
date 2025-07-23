import csv

# Open and read the CSV file
with open("customers.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Headers:", header)

    for row in reader:
        # Example cleanup: strip whitespace from each value
        cleaned_row = [value.strip() for value in row]
        print("Cleaned row:", cleaned_row)

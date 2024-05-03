import csv
from prettytable import PrettyTable
table = PrettyTable()



def read(target_file):
  with open(target_file , "r", newline="") as file:
    reader = csv.reader(file)

    # Extract field names (headers) from the first row (optional)
    headers = next(reader)  # Assuming headers are in the first row

    # Create a PrettyTable object
    table = PrettyTable(headers) if headers else PrettyTable(reader.fieldnames)

    # Add each row as a dictionary
    for row in reader:
      
      table.add_row(list(row))


    

  # Print the formatted table
  print(table)
      
    
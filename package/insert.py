import csv

# data = [[6,"CTO","Kupe","06/01/2024",400000]]

def insert(target_file):
  
  try:
    with open(target_file, "a", newline="") as csvfile, open("./inputs/insert.csv", "r", newline="") as input_file:
      writer = csv.writer(csvfile)

      reader = csv.reader(input_file)
      
      # Skip first row i.e headers.
      next(reader)
      for row in reader:
        # print(row)
        writer.writerow(row)
  except FileNotFoundError:
    print("File not found")
  finally:
    print("Inserted sucessfully")
    
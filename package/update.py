import csv

def update(target_file):
  """
    Read update.csv file
    Read target.csv file
    Now loop over target_file_rows
      if row["id"] == [update_file]

  """
  with open(target_file, "r")as target_csv_file, open("inputs/update.csv", "r") as update_csv_file, open("inputs/update.csv", "r") as update_csv_temp:
    
    target_reader = csv.DictReader(target_csv_file)
    update_reader_temp = csv.reader(update_csv_file)
    update_reader = csv.DictReader(update_csv_file)
    
    # target_header = next(update_reader_temp)[0] # id
    # print(target_header)
    
    
    
    ids = [row["emp_id"] for row in update_reader]

    for row in target_reader:
      # print(row["emp_id"])    
      if row["emp_id"] in ids:
        print(row)
        
    

      


    
  # numbers = [1, 2, 3, 4, 5]
  # # squares = [number * number for number in numbers]
  # # print(squares)
  # # even_numbers = [number for number in numbers if number%2 == 0]
  # even_numbers = [number for number in numbers]
  # print(even_numbers)
  
  
  # return 

import csv

def update(target_file):
  
  # get data from csv
  updating_date = get_data_from_csv()
  whom_to_target= list(updating_date.keys())[0]
  whom_to_target_value = list(updating_date[whom_to_target])[0]
  # print(type(whom_to_target), type(whom_to_target_value))
  
  what_to_update = list(updating_date.keys())[1]
  what_to_update_with = updating_date[what_to_update]
  # print(type(what_to_update), type(what_to_update_with))
  
  # return
  updated_data = []
  with open(target_file, "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row[f"{whom_to_target}"] == f"{whom_to_target_value}":
        row[f"{what_to_update}"] = f"{what_to_update_with}"
      updated_data.append(row)

  with open(target_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(updated_data)

def get_data_from_csv():
  # read file inputs/update.csv
  # get data from it.
  with open("./inputs/update.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      # print(row)
      return row
      
        
  
  

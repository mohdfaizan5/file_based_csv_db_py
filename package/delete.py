# def delete():

#   deleting_id = [3]

#   ids = [
#     {
#     "id": 1,
#     "name": "s"
#   },
#     {
#     "id": 2,
#     "name": "s"
#   },
#     {
#     "id": 3,
#     "name": "s"
#   },
#     {
#     "id": 5,
#     "name": "s"
#   },
#         ]

#   for row in ids:
#     if row['id'] not in deleting_id:
#       print(row)
    


import csv

final_data = []

def delete(target_file):
  """"""
  with open(target_file, "r+") as target, open("./inputs/delete.csv", "r") as input_file:
    reader = csv.DictReader(target)
    input_reader = csv.reader(input_file)
    # writer = csv.DictWriter(target) # field names are required
    
    
    target_header = next(input_reader)[0]
    print(target_header)
    
    targeted_values = []
    for r in input_reader:
      targeted_values.append(int(r[0]))
    print(targeted_values)
    
    
    for row in reader:
      # print(type(row["emp_id"]))
      if(int(row[target_header]) not in targeted_values):
        
        print(row["emp_id"])
        print(row)
        writer.writerow(row)
        # Here I got final values 
    
    # Now take that values and write to target.csv
    #
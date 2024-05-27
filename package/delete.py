import csv

final_data = []

def delete(target_file):

  with open(target_file, "r") as target_read, open("./inputs/delete.csv", "r") as input_file, open(target_file, "r+") as temp_read:
    
    reader = csv.DictReader(target_read)
    reader_temp = csv.DictReader(temp_read)
    input_reader = csv.reader(input_file)
    
    target_header = next(input_reader)[0]
    
    targeted_values = []
    for r in input_reader:
      targeted_values.append(r[0])
    
    headers = []
    for row in reader_temp:
      headers = list(row.keys())
      break
    
    # print(headers)
    final_data.append(headers)
    
    # print(final_data)
    for row in reader:
      
      if(row[target_header] not in targeted_values):
        # print(list(row.values()))
        final_data.append(list(row.values()))
        
    # Here I got final values 
    # print(final_data)
    

    with open(target_file, "w", newline="") as final_file:
      
      writer = csv.writer(final_file) # field names are required
    
      for row in final_data:
        writer.writerow(row)  
        
    print("Deleted successfully")
      
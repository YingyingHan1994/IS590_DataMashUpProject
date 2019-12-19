import json
import csv
with open('princeton_clean7_nonelist.json', 'r') as fin:
    data = json.load(fin)
print(len(data))

# Replace records of which the state value is null to "missing"
for records in data:
    #print(records)
    #print(records["State"])
    if records["State"] == None:
        records["State"] = "missing"
    #print(records["State"])
    #print(records["City"])
# Replace records of which the state value is null to "missing"
    if records["City"] == None:
        records["City"]="missing"
    print(records["City"])
# Write the results out in a csv file named "princeton_clean11_nonlist.csv"
keys = data[0].keys()
with open('princeton_clean11_nonlist.csv', 'w',encoding = "utf-8") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)




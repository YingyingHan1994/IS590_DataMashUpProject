import json

# Read the json file and check the length of the file to make sure I read the right file.
with open('princeton_clean2_removegeocode.json', 'r') as fin:
    data = json.load(fin)
print(len(data))
print(type(data))

# Delete the duplicated lines. Create an empty list. if the record has appeared, continue running.
# If the record is firstly appeared, append that record to the list.
list = []
for records in data:
    if records in list:
        continue
    else:
        list.append(records)
#print(list)

# Write the results out to file princeton_clean3_removeduplicates.json
with open('princeton_clean3_removeduplicates.json', 'w') as f:
    json.dump(list, f)











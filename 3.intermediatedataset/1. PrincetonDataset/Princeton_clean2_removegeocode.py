import json

# Read the json file
with open('princeton_clean1_deletenull.json', 'r') as fin:
    data = json.load(fin)


# The json file is read as a dictionary with one key "RECORDS" and all the records are the value of the key.
# So, I will read all the records and check how many records are there in this file by checking the length of the data
princeton = data["RECORDS"]
print(len(princeton))

# Princeton is a list of dictionary, and each dictionary is a record of an object geography information.
# Match and find out those record of which the GeoCode is "Place depicted".
# Once find out that record, delete that record.
# Append the left records as dictionaries in a list.
# 7462 records are deleted
list = []
for dics in princeton:
    #print(dics["GeoCode"])
    if dics["GeoCode"] == "Place depicted":
        del dics
    else:
        list.append(dics)
print(len(list))

# Match and find out those record of which the GeoCode is "(not assigned)".
# Once find out that record, delete that record.
# Append the left records as dictionaries in a list.
# 17 records are deleted.
list1= []
for dics in list:
    #print(dics["GeoCode"])
    if dics["GeoCode"] == "(not assigned)":
        del dics
    else:
        list1.append(dics)
print(len(list1))

# Match and find out those record of which the GeoCode is "Geographic Attribution".
# Once find out that record, delete that record.
# Append the left records as dictionaries in a list.
# 9 records are deleted.
list2 = []
for dics in list1:
    if dics["GeoCode"] == "Geographic Attribution":
        del dics
    else:
        list2.append(dics)
print(len(list2))

# Write the results out to file princeton_clean2_removegeocode.json
with open('princeton_clean2_removegeocode.json', 'w') as f:
    json.dump(list2, f)

# Check if the length of the file is 6163 to make sure all the results have been written out!
with open('princeton_clean2_removegeocode.json', 'r') as fin:
    data = json.load(fin)
print(len(data))






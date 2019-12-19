# Read the file GM_clean5_RemoveDuplicate_ObjectID_RemoveEmptyLine.csv in
# Then I read the fourth and fifth column, which is the latitude number and longitude number respectively.
# I turn the latitude number and longitude number to float number.
# I write the result in a list named data.
import csv
with open('GM_clean5_RemoveDuplicate_ObjectID_RemoveEmptyLine.csv', 'r') as f:
    csv_data = next(csv.reader(f), None)          # Skip first row
    data=[(float(line[4]), float(line[5])) for line in csv.reader(f) if line]
#print(data)
#print(len(data)) result is 3553

# import reverse-geocoder package and run every records in data through this package.
# Then I write the result in a new list named "list1"

list1 = []
import reverse_geocoder as rg

for records in data:
    results = rg.search(records, mode =1)
    list1.append(results)
# print(len(list1)) the result is 3553.

# Each record in list 1 is a list, the first index of which is an ordered dictionary.
# I want to transfer it to be a dictionary so that I can better write the result out!
# I firstly write the ordered dictionaries into a new list named "list2"

list2 = []
for records in list1:
    # print(records)
    #print(type(records))
    # print(records[0])
    # print(type(records[0]))
    list2.append(records[0])
#print(len(list2)) the result is 3553

# Now I want to turn each record in list2 from an ordered dictionary to a dictionary.
# Each dictionary will be append to a new list named "list3"
list3 = []
for records in list2:
    records_dic = dict(records)
    list3.append(records_dic)
# print(len(list3)) The result is 3553.

# List 3 is a list in which each record is a dictionary. In each dictionary, there is a record of the city, state, country.
# Ready to write the list 3 out to a csv file. The header of the csv file is dictionary keys. The value of the dictionaries will be in the cells.
# Firstly, I will get the keys out from a dictionary.
# The result is in a csv file named "gm_clean7_fromlatitudelongitudetolocation.csv"
keys = list3[0].keys()
with open('gm_clean7_fromlatitudelongitudetolocation.csv', 'w',encoding = "utf-8") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list3)










# Open the file####################################
import json
import csv
with open('princeton_clean7_withlonglatitude.json', 'r') as fin:
    data = json.load(fin)
    print("length of data",len(data))


# # In the file, some of the records of which the latitude value include an unidentifiable character "掳". I need to delete those records.

# In[53]:


list = []
for records in data:
#     if "掳" in records["Longitude"]:
#         records.clear()
    latitude = records["Latitude"]
    longitude = records["Longitude"]
    #print(latitude, longitude)
    
    if "掳" in records["Longitude"]:
        continue
    else:
        list.append(records)
print("length of list",len(list))

       


# # Extract the longitude/latitude number and turn them first to be float, then tuple so that I can run them through reverse_geocoder package. 

# In[70]:


list1=[]
for records in list:
    latitude = records["Latitude"]
    longitude = records["Longitude"]
    latitude_number = float(latitude)
    longitude_number = float(longitude)
    location = [latitude,longitude]
    #print(location)
    number = tuple(location)
    list1.append(number)
print("length of list1",len(list1))

# Import reverse_geocoder package
import reverse_geocoder as rg 
# import pprint

# Run every longitude, latitude tuple through the pack and get the results in list2.
list2 = []
for records in list1:
    #print(records)
    results = rg.search(records,mode=1)
    list2.append(results)
    #print(results)
print("length of list2",len(list2))

# Each record in list2 is a list, the first index of which is an ordered dictionary.

list3 =[]
for records in list2:

    list3.append(records[0])
    #print(type(records[0]))
print("length of list 3",len(list3))

# I want to transfer it to be a dictionary so that I can better write the result out!
from collections import OrderedDict

list4 = []
for records in list3:
    records_dic = dict(records)
    list4.append(records_dic)
print("the length of list4", len(list4))

#Writet the list out to a csv file named "princeton_clean9_withlongitudelatitude.csv"
keys = list[0].keys()

with open('princeton_clean9_withlongitudelatitude.csv', 'w',encoding = "utf-8") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list)

#Writet the list4 out to a csv file named "princeton_clean9_transferlocation.csv"

keys = list4[0].keys()
print(keys)

with open('princeton_clean9_transferlocation.csv', 'w',encoding = "utf-8") as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list4)

# for key, value in records.items():
#     d[key] = value
#     print(d)
#     list4.append(d)
#         #print(d)
# print("length of list4",len(list4))


# for records in list4:
#     print(records)

# for records in data:
#     records.update
# list4=[]
# for records in data:
#     for dictionary in list3:
#         records.update(dictionary)
#         list4.append(records)
# print(len(list4))
# # for records in list4:
# #     #print(records)









import json

# Read the json file.
with open('princeton_clean3_removeduplicates.json', 'r') as fin:
    data = json.load(fin)
    #print(len(data))

# replace the continent value “Europe?” as “Europe”. (2 records have been replaced)
for records in data:
    #print(records)
    if records["Continent"] == "Europe ?":
        #print(records)
        records["Continent"] = "Europe"
    # replace the continent value “Ellis Island” as “North America”. (1 record have been replaced)
    if records["Continent"] == "Ellis Island":
        #print(records)
        records ["Continent"] = "North America"
    #print(records["Continent"])
    # replace the continent value “Central America” as “North America”. (6 records have been replaced)
     #According to the information on the Internet, the Central America is apart of the North America.
    if records["Continent"] == "Central America":
        #print(records)
        records["Continent"] = "North America"
    # replace the continent value “Providence” as “North America”. (1 record have been replaced)
    if records["Continent"] == "Providence":
        #print(records)
        records["Continent"] = "North America"
    # print(records["Continent"])
    # print(type(records["Continent"]))
    # In the json file, the continent value is "null". While the json file is read in, the null value is changed to be "None". None is a object of Nonetype.
    if records["Continent"] == None:
        # if (records["Country"])== None:
        #     print(records)
        #The counrty values include "United States", "Mexico","None"
        # For those 4 records of which both Continent and country values are none, One record includes city value "Stoke-Upon-Trent", which is a city in England. One record includes
        # city value "Burslem", which is a city in England. The other two records include the same latitude number and longitude number (40.3476. -74.6576). According to https://www.latlong.net/Show-Latitude-Longitude.html, the location is Princeton in the United States, New Jersey.
        # I am turning all the records of which Continent value is None to "North America" and later change the value of the records of which city values are ""Stoke-Upon-Trent" and Burslem"
        records["Continent"] = "North America"
    if records["City"] == "Stoke-Upon-Trent":
        records["Continent"] = "Europe"
        records["State"] = "The West Midlands"
    if records["City"] == "Burslem":
        records["Continent"] = "Europe"
        records["State"] = "The West Midlands"

# Check if the Continent value is clean now.
# list = []
# for records in data:
#     if records["Continent"] in list:
#         continue
#     else:
#         list.append(records["Continent"])
# print(list)
#result is ['North America', 'Europe', 'Asia', 'South America', 'Africa']

# Write the results out in file princeton_clean4_typofixed.json.
with open('princeton_clean4_typofixed.json', 'w') as f:
    json.dump(data, f)







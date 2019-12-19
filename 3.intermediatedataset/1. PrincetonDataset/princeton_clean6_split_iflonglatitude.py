import json

# Read the json file
with open('princeton_clean5_countryvaluefixed.json', 'r') as fin:
    data = json.load(fin)

nonelist = []
for records in data:
    #print(records)
    #print(records["State"])
# Check the record of which the state value is "probably Chiapas". Re-check its state information according to the given latitude/longitude number.
#     if records["State"] == "probably Chiapas":
#         #print(records)
#         records["State"] = "San Luis Potosi"
#         records["City"] = "Villa de Ramos"
#     # if records["State"] == "probably Chiapas":
#     #     print(records)

    #print(records)
    latitude = records["Latitude"]
    longitude = records["Longitude"]
    if latitude == None:
        nonelist.append(records)
#print(nonelist)
#print(len(nonelist)) the result 1126

    if longitude == None:
        nonelist.append(records)
#print(nonelist)
#print(len(nonelist)) the result is 3420

# Now, the nonelist include records either latitude number is none or longitude is none. This might includes three cases:
# (1) longitude and latitude are both none. (2)Longitude is none but latitude is not.
# (3) Latitude is none but longitude is not
# Delete the duplicates in the nonlist

nonelist_deleteduplicates = []
for records in nonelist:
    if records in nonelist_deleteduplicates:
        continue
    else:
        nonelist_deleteduplicates.append(records)
# print(nonelist_deleteduplicates)
# print(len(nonelist_deleteduplicates))

#Write the nonlist_deleteduplicates out in a json file names "princeton_clean7_nonelist.json"
import json
with open('princeton_clean7_nonelist.json', 'w') as foute:
    json.dump(nonelist, foute)


# Write the records with longitude number and latitude number out in a file names "princeton_clean7_withlongitudelatitude.json
longlatitudelist = []
for records in data:
    if records in nonelist_deleteduplicates:
        continue
    else:
        longlatitudelist.append(records)
# print(longlatitudelist)
# print(len(longlatitudelist))

import json
with open('princeton_clean7_withlonglatitude.json', 'w') as fout:
    json.dump(longlatitudelist, fout)









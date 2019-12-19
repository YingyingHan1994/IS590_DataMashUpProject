import json

# Read the json file
with open('princeton_clean4_typofixed.json', 'r') as fin:
    data = json.load(fin)

for records in data:
    #print(records["Country"])

    # Modify the country value from "United State" to "United States"
    if records["Country"] == "United State":
        #print(records)
        records["Country"] = "United States"

    # Modify the country value from "North America" to "United States".
    if records["Country"] == "North America":
        #print(records)
        records["Country"] = "United States"

    # Modify the country value from "Mexico or Guatemala" to "Mexico". I can do this because the longitude numnber/latitude number is given, and country name can be calculated from https://www.latlong.net/Show-Latitude-Longitude.html
    if records["Country"] == "Mexico or Guatemala":
        #print(records)
        records["Country"] = "Mexico"
        records["State"] = "Nuevo Leon"
        records["City"] = "General Terán"

    # Modify the country value from "Guatemala or Mexico" to either "Guatemala" or "Mexico" according to the given longitude and latitude number.
    if records["Country"] == "Guatemala or Mexico":
        #print(records)
        if records["ObjGeographyID"] == 675:
            records["Country"] = "Mexico"
            records["State"] = "Zacango"
            records["City"] = "Calimaya"


        if records["ObjGeographyID"] == 699:
            records["Country"] = "Mexico"
            records["State"] = "Nuevo Leon"
            records["City"] = "General Terán"

        if records["ObjGeographyID"] == 707:
            records["Country"] = "Mexico"
            records["State"] = "Nuevo Leon"
            records["City"] = "General Terán"

        if records["ObjGeographyID"] == 708:
            records["Country"] = "Mexico"
            records["State"] = "Nuevo Leon"
            records["City"] = "General Terán"

        if records["ObjGeographyID"] == 10:
            records["Country"] = "Guatemala"
            records["State"] = "El Petén"
            records["City"] = "San Benito"

        if records["ObjGeographyID"] == 467:
            records["Country"] = "Mexico"
            records["State"] = "Nuevo Leon"
            records["City"] = "General Terán"

# Replace the country value from 'probably Guatemala' to “Guatemala” and add state, city information
# according to the given longitude and latitude number.
# The given location is 'Latitude': '15.5', 'Longitude': '-90.25, it is located in
# San Pedro Carchá (city), Alta Verapaz (state), Guatemalan (country)
    if records ["Country"] == "probably Guatemala":
        records["Country"] = "Guatemala"
        records ["City"] = "San Pedro Carchá"
        records ["State"] = "Alta Verapaz"

#Replace the country value from 'possibly Guatemala' to “Guatemala” and add the city, state information according to the given longitude/latitude number. 1 record is changed.
    if records ["Country"] == "possibly Guatemala":
        #print(records)
        records["Country"] = "Guatemala"
        records ["City"] = "San Pedro Carchá"
        records ["State"] = "Alta Verapaz"

# Replace the country value from 'Mexico, Guatemala, or Belize' to “Mexico” and add the city, state information according to the given longitude/latitude number. 1 record is changed.
    if records ["Country"] == "Mexico, Guatemala, or Belize":
        #print(records)
        records["Country"] = "Mexico"
        records["State"] = "Nuevo Leon"
        records["City"] = "General Terán"

# Replace the country value from 'Northern Belize or Quintana Roo, Mexico' to “Mexico” and add the city, state information according to the given longitude/latitude number. 1 record is changed.
    if records ["Country"] == "Northern Belize or Quintana Roo, Mexico":
        #print(records)
        records["Country"] = "Mexico"
        records["State"] = "Nuevo Leon"
        records["City"] = "General Terán"

# Replace the country value from 'Belize, Guatemala, or Mexico' to “Mexico” and add the city, state information according to the given longitude/latitude number.7 records have been changed.
    if records ["Country"] == "Belize, Guatemala or Mexico":
        #print(records)
        records["Country"] = "Mexico"
        records["State"] = "Nuevo Leon"
        records["City"] = "General Terán"
# Replace the country value from 'Belize, Guatemala or Mexico' to  “Mexico” and add the city, state information according to the given longitude/latitude number.  4 records have been changed.
    ## ATTENTION: In line 92, I already clean the country value "Belize, Guatemala or Mexico". Here I am cleaning the country value "Mexico, Guatemala, or Belize". There is a comma before "or".
    if records ["Country"] == "Mexico, Guatemala, or Belize":
        #print(records)
        records["Country"] = "Mexico"
        records["State"] = "Nuevo Leon"
        records["City"] = "General Terán"

# For the records of which country value is "null", which is read as "None" in this file, I will check their given longitude/latitude number or GeoNames
# To get the country, state, city names.
# If there is neither longitude/latitude number nor GeoNames, the country, state, city values are missing.
    if records ["Country"] == None:
        if records ["GeoNames"] == "www.geonames.org/2614165/scandinavia.html":
            #print(records)
            records ["Country"] = "Norway"
            records ["State"] = "Trøndelag"
            records ["City"] = "Tydal"


        if records ["GeoNames"] == "www.geonames.org/6255148/europe.html":

            records ["Country"] = "German"
            records ["State"] = "Baden-Württemberg"
            records ["City"] = "Leinfelden-Echterdingen"

        if records ["GeoNames"] == "http://www.geonames.org/6255148/europe.html":
            #print(records)
            records ["Country"] = "German"
            records ["State"] = "Baden-Württemberg"
            records ["City"] = "Leinfelden-Echterdingen"

        if records["ObjGeographyID"] == 17860:
            records["Country"] = "England"

        if records["ObjGeographyID"] == 17887:
            #print(records)
            records["Country"] = "England"

        if records["ObjGeographyID"] == 775:
            #print(records)
            records ["Country"] = "missing"
            records ["State"] = "missing"
            records ["City"] = "missing"

        if records["GeoNames"] == "http://www.geonames.org/7729892/central-america.html":
            #print(records)
            records["Country"] = "Mexico"
            records["State"] = "Nuevo Leon"
            records["City"] = "General Terán"
        if records["ObjGeographyID"] == 195:
            #print(records)
            records ["Country"] = "missing"
            records ["State"] = "missing"
            records ["City"] = "missing"

        if records["ObjGeographyID"] == 7:
            #print(records)
            records ["Country"] = "missing"
            records ["State"] = "missing"
            records ["City"] = "missing"

        if records["ObjGeographyID"] == 35108:
            #print(records)
            records ["Country"] = "United States"
            records ["State"] = "New Jersey"
            records ["City"] = "Princeton"

        if records["ObjGeographyID"] == 7:
            #print(records)
            records ["Country"] = "United States"
            records ["State"] = "New Jersey"
            records ["City"] = "Princeton"

# Write the results out!
with open('princeton_clean5_countryvaluefixed.json', 'w') as f:
    json.dump(data, f)















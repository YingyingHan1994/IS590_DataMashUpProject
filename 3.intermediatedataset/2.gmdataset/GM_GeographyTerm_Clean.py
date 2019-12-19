# import pandas and csv
import pandas as pd
import csv

# Read the file in using pd.read_csv function
GeographyFile = pd.read_csv("gm_geography_clean1_columndelete.csv",encoding="Latin-1")

#print(GeographyFile.head())

#print(GeographyFile.shape)

# I learn the following scripts from https://www.youtube.com/watch?v=2AFGPdNn4FM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=8.
# Read the ThesXrefType value and
# check out those records of which GonGeoCode values are“Place found” and “Place Made”.
# I created a list. If the geocode value is either "“Place found” or “Place Made”, a true value will be append to the list.
# Otherwise, a False value will be appended.
# By doing that, I created a python boolean list telling us which row matches the conditions.
booleans = []

for term in GeographyFile.ThesXrefType:
    if term == "Place found":
        booleans.append(True)
    elif term == "Place Made":
        booleans.append(True)
    else:
        booleans.append(False)

# Convert a boolean list to a pandas series.
GeographyTerm = pd.Series(booleans)
#print(GeographyTerm)

Clean_GeographyTerm =GeographyFile[GeographyTerm]

#print(Clean_GeographyTerm)
# Write the results out in a file named GM_Clean2_CorrectGeographyTerm.csv
Clean_GeographyTerm.to_csv("GM_Clean2_CorrectGeographyTerm.csv")


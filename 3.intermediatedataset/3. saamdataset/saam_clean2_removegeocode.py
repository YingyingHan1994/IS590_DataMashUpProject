# import pandas and csv
import pandas as pd
import csv


# Read the file in using pd.read_csv function
geographyfile = pd.read_csv("saam_WebConGeography_CleanDataRemoveDuplicates.csv",encoding="Latin-1")

# I learn the following scripts from https://www.youtube.com/watch?v=2AFGPdNn4FM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=8.
# Read the GonGeoCode value and
# check out those records of which GonGeoCode values are“Place of Birth” and “Place of Death”.
# I created a list. If the geocode value is either ""Place of Birth" or "'Place of Death'", a true value will be append to the list.
# Otherwise, a False value will be appended.
# By doing that, I created a python boolean list telling us which row matches the conditions.
booleans = []
# geographyfile.ConGeoCode is a panda series, which is ilterable.
for geocode in geographyfile.ConGeoCode:
    #print(geocode)
    if geocode == "Place of Birth":
        booleans.append(True)
    elif geocode == 'Place of Death':
        booleans.append(True)
    else:
        booleans.append(False)

# Convert a boolean list to a pandas series.
GeographyTerm = pd.Series(booleans)
#print(GeographyTerm)
clean_geographyterm =geographyfile[GeographyTerm]
#print(clean_geographyTerm)

# Write the results out in a file named saam_clean2_correctgeographyterm.csv
clean_geographyterm.to_csv("saam_clean2_correctgeographyterm.csv")






#import packages
import pycountry_convert as pc
import csv
import pandas

# from the package import different functions.
# "country_alpha2_to_continent_code" can convert country code ISO 3166-1 alpha-2 to continent code.
# “country_alpha2_to_country_name" can convert country code ISO 3166-1 alpha-2 to to country name.
# "convert_continent_code_to_continent_name" can convert continent code to continent name
from pycountry_convert import country_alpha2_to_continent_code,convert_continent_code_to_continent_name,country_alpha2_to_country_name

# Define functions
# The first function can converse the entered country code ISO 3166-1 alpha-2 to continent name.
# The second function can converse the entered country code ISO 3166-1 alpha-2 to country name.
def countrycode_to_continent(country_alpha2):
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

def countrycode_to_country(country_alpha2):
    country_name = pc.country_alpha2_to_country_name(country_alpha2)
    return country_name

#Test
# code = 'CA'
# print(countrycode_to_continent((code)))
# print(countrycode_to_country(code))


# Now I need to read the country code column into a list
# import csv and pands
# cc is the coloumn name of the country code
colnames = ["cc"]
data = pandas.read_csv('gm_clean7_fromlatitudelongitudetolocation.csv', names=colnames,skiprows =1)
country_code = data.cc.tolist()
# print(country_code)
# print(len(country_code))

# Now, I want to run every code through the above-mentioned functions and get the continent and country names.
# I will append continent and country names into two different lists.
continent_list = []
country_list = []
for code in country_code:
    continent = countrycode_to_continent(code)
    country_name = countrycode_to_country(code)
    continent_list.append(continent)
    country_list.append(country_name)
# print(len(continent_list))
# print(len(country_list))

# Now, I am ready to write the two lists out two different csv files: gm_clean8_continent.csv and gm_clean8_country.csv
# Write the continents out!
outfile = open ("gm_clean8_continent.csv","w",encoding='utf-8')
csvout =csv.writer(outfile)
csvout.writerow(["Continent"])

for con in continent_list:
    row = [con]
    csvout.writerow(row)

# Write the country out!
outfile1 = open("gm_clean8_country.csv","w",encoding='utf-8')
csvout =csv.writer(outfile1)
csvout.writerow(["Country"])

for coun in country_list:
    row1= [coun]
    csvout.writerow(row1)






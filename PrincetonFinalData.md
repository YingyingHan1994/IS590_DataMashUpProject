## Data Collection
Princeton University Art Museum dataset is downloaded from https://github.com/american-art/PUAM.
The raw data is in json format. The file name is "PrincetonUniversityRawData.json"

## Data processing
The raw code was processed by code script named "Json_tool_test2.py" and "json_profile_tools.py". After data processing, data documentation is finished.
Please check out data documentation here: https://github.com/YingyingHan1994/IS590_DataMashUpProject/blob/master/Princeton%20Data%20Documentation.md.

## Data format transfer
The raw json file is transferred to csv by a code script named "JsonToCSV_Panda.py"
The output file is named "PrincetonUniversityRawData.csv"

## Data cleaning
The data cleaning process include:
Clean the raws that all attribute values are “null”. (Done)

Delete those rows of which the geocode value is “place depicted”, “not assigned”, “geography attribution”, “null”. 

“Geography attribution” there are 7 records according to data documentation but I found 10 records in the csv file. (Done)

“Not assigned”, delete 7 records (Done).

“Place depicted”, delete 101 records. (Done)

Delete the duplicates line. The outfile names “PricetonUniversityCleanDataRemoveDuplicates.csv”
delete two records of which the value is “Europe?”. (Done)

Regarding the six records of which the continent is “America”, further determine if they are from “North America”, “South America”, or “Central America” and document the decision-making process. (Not done)

Change the record of which the continent value is “paris” to “European”. (Done)

Modify the record of which the continent value is “noth America” to “North America”. (Done)

Modify the record of which the continent value is “Ellis Island” to “North America”.(Done)

Modify the record of which the continent value is “San Mateo County” to “North America”. (Done)

Modify the record of which the continent value is “Providence” to “North America”. (Done)

Modify the record of which the continent value is “Union County” to “North America”. (Done)

Modify the record of which the continent value is “Union County” to “North America”. 

Modify the record of which the continent value is “Delphi” and “New York” to “North America”. (Done)

Modify the record of which the continent value is “Florence” to “Europe”. (Done)

Modify the record of which the continent value is “Australia” to “Oceania”. (Done)

Modify the record of which the continent value is “Asia Minor” to “Oceania”. (Done)

Remove the duplicated rows using scipt named "Princeton_DataCleaning_RemoveDuplicates.py"
The final output file names "PricetonUniversityCleanDataRemoveDuplicates.csv"

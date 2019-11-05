# 1.Data cleaning assessment
No data cleaning is needed.
# 2.Describe the authorship, attribution, and/or the provenance of the file.  
To be filled up.
# 3. Describe the semantic contents of the file.

## 3.1 A short plain language statement about what the data file contains, this should be very much along the lines of a domain description.
The file describes where the constituents were born. It includes the constituent ID, city, country, state, geocode.

## 3.2 A short statement about what is being used from this dataset.
1. The file named "WebConGeography", which describes the artisits' born/death geography information is to be used.
2. Extract those records of which the geocode is "associated place", "associated place (at time of NEA award)", "last known residence", "place of birth". Analyze the country and state information.
## 3.3 Relevant dates of the data collection.
24 October, 2019

# 4 Describe the collection process.
The data was collected from:https://github.com/american-art/SAAM

# 5 Description of the data structure
## 5.1 What data format is this file stored in?
The data model is stored in the format of dot, json, md, pdf, ttl and n3. The data is stored in the format of csv.
## 5.2 What are the records/entities within this data file? What do they represent?  Imagine this describing what a single row in a CSV represents.
Each row describes where the artist was born and died. The artist is identified by constitute ID. The geography information is described from the aspects of city, country, state, county. Geocode tells the information what type of the geography information is given (for example, place of birth).


# 6 Codebook
## 6.1 Description of column (a short human readable statement of what this column contains).
See my answer to question 5.2. 
## 6.2 Description of data values and units present
Constituent ID: there are 7453 unique values and no missing value. Each value represent an artist. However, there are 16199 lines with Constituent ID, which means that some Constitutent ID is repeated in the file. 

City: There are 3647 unique values and no missing value. 

County: There are 124 unique values and no missing value. 

State: There are 158 unique values and no missing value.

Country: There are 129 unique values and no missing value.

Congeocode: There are 6 unique values and the values are: not assigned, associated place, associated place (at time of NEA award), last known residence, place of birth, place of death.
## 6.3 What are all the unique values and their meaning? (if you have categorical data).  Don’t do this if there are more than like 10 or 20.
See my answer to question 6.2.
## 6.4 Reason for missing values and the relevant missing values or codes
No missing value.
## 6.5 Number of known missing values within this column
Not applicable. 
## 6.6 Other notes, caveats, attribution, etc. that you need to report for this data file.
None.

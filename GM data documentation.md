# 1.Data cleaning assessment
1. Delete records of which the reference type is "0900".
2. The geogography terms include four type: culture area (2577 records), place, place made (1004), place found (7985 records). There are 10668 rows in this csv file. Each raw has one object ID value. While there are only 4239 unique object ID values. This shows that many object geography information is repeated in this file. The object ID value is repeated because of two reasons: the museum might record the "found place", "made place", "culture area" of an object, so they will repeat the different types of geograpphy information in different rows. In this case, I want to keep the rows the geography term is either "place made" or "place found". I decided to sacrifice the number of the records for a more accurate dataset.
The second reason why object ID is repeated in different rows is the musuem sometime records two "found place" or "made place" for one object. For example, the object of which the ID is 14721 was found in Mexico and Nayarit. Nayarit is actually a state in Mexico. ??  
3. For those object of which state/city information is given, map the location to their country. Or map the longitude/latitude numbers to counrty. If so, I need to devide the file into two parts: records with longitude and latitude numbers and those with no longitude and latitude information. 

# 2.Describe the authorship, attribution, and/or the provenance of the file.  
The dataset was created and published by Gilcrease Museum. It is published under the terms of the Creative Commons CC0 1.0 Universal Public Domain Dedication and can be freely re-used for any purpose.
# 3. Describe the semantic contents of the file.

## 3.1 A short plain language statement about what the data file contains, this should be very much along the lines of a domain description.
The Gilcrease Museum describes its geography information from the aspects of country, or state, or city, and longitude number, latitude number, longitude direction, latitude direction. However, country, state, city names are fixed in one column. 
## 3.2 A short statement about what is being used from this dataset.
The country, state, city information, longitude number, latitude number.
## 3.3 Relevant dates of the data collection.
24 October 2019

# 4 Describe the collection process.
The data was downloaded from https://github.com/american-art/GM.

# 5 Description of the data structure
## 5.1 What data format is this file stored in?
The data is stored in the csv format.
## 5.2 What are the records/entities within this data file? What do they represent?  Imagine this describing what a single row in a CSV represents.
In each row, the object is identified by an object ID. The object ID is repeatable in different rows. The reference type illustrates the type of geography information, such as "place found". The specific geography information is represented by longitude number, latitude number, longitude direction, latitude direction.

# 6. Describe the dimensions of the data. How many records are there? How many properties about each record are there?

# 6.1 “Geography.csv”. 
There are 10668 records. Each record has the nine properties, including object ID, term, reference type, latitude, longitue, latitude direction, longitude direction, latitude number, longitude number.

## 6.2 What sort of data types are present within the data file? Describe this in plain human language. For example, integer, categorical, etc.
ObjectID: integer
Term: string
Reference Type: string
Latitude Number: float
Longitude Number: float

# 7 Codebook
## 7.1 Description of column (a short human readable statement of what this column contains).
1. object ID: An object is assigned with an ID, which uniquely represents the object.
2. Term: the geography area (country, or state, or city).
3. Reference Type: The type of geography information
4. Latitude: for example, 23.00
5. latitude direction: N,S,W,E represent North, South, West, and East respectively.
6. Longitude: for example, 102.
7. Longitude direction: N,S,W,E represent North, South, West, and East respectively.
8. Latitude number: for example, 23.00
9. Longitude number: for example, -102.00
## 7.2 Description of data values and units present 
Object ID: 4239 unique values from 10668 records. I identify two reasons for repeated object ID. 
Term: 635 unique values.
Reference type: 5 unique values, which are 0900, cultural area, place, place made, place found. 

## 7.3 What are all the unique values and their meaning? (if you have categorical data).  Don’t do this if there are more than like 10 or 20.
See my answer to question 7.2.

## 7.4 Reason for missing values and the relevant missing values or codes
Though the csv parser tool shows that there is no missing data in each column. However, it is observed that several columns do not have longitude/latitude number. 

## 7.5 Number of known missing values within this column
3421 records with no longitude number, latutude number, or the number is 0.

## 7.6 Other notes, caveats, attribution, etc. that you need to report for this data file.
No.

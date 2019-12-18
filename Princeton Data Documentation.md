# 1.Data cleaning assessment
1. Delete the records, all the properties of which are “null”. 8079 records out of 21730 records should be deleted. 
2. Delete the repeated records. If the geography ID and object ID of two records are the same, the two records are identified as the same record. 
3. In terms of the data value for continent, delete two records of which the value is “Europe?”. Regarding the six records of which the continent is “America”, further determine if they are from “North America”, “South America”, or “Central America” and document the decision-making process. Change the record of which the continent value is “paris” to “European”. Modify the record of which the continent value is “noth America” to “North America”. Modify the record of which the continent value is “Ellis Island” to “North America”. Modify the record of which the continent value is “San Mateo County” to “North America”. Modify the record of which the continent value is “Providence” to “North America”. Modify the record of which the continent value is “Union County” to “North America”. Modify the record of which the continent value is “Delphi” and “New York” to “North America”. Modify the record of which the continent value is “Florence” to “Europe”. Modify the record of which the continent value is “Australia” to “Oceania”. Modify the record of which the continent value is “Asia Minor” to “Oceania”. 
4. I will delete the file using python and do the modification of the records on my own by hand. In all, I need approximately 1.5 hours for data cleaning. 


# 2.Describe the authorship, attribution, and/or the provenance of the file.  
The dataset was created and published by Princeton University Art Museum. It is published under the terms of the Creative Commons CC0 1.0 Universal Public Domain Dedication and can be freely re-used for any purpose.

# 3. Describe the semantic contents of the file.

## 3.1 A short plain language statement about what the data file contains, this should be very much along the lines of a domain description.
The Princeton University Art Museum described their collection from four aspects: object, artist, exhibition, digital object. The object information is connected to the exhibition information, digital object information, and artist information via object ID. In the following parts, I introduced the dimensions of object, artist, exhibition, digital object information in details. 


## 3.2 A short statement about what is being used from this dataset.
The geography file is analyzed, including the geocode information, continent, and country information. 
## 3.3 Relevant dates of the data collection.
10/24/2019

# 4 Describe the collection process.
The data is downloaded from https://github.com/american-art/PUAM.

# 5 Description of the data structure
## 5.1 What data format is this file stored in?
Data model is saved in multiple formats, including dot, json, md, pdf, ttl, n3. The data set is saved in the format of json. 

## 5.2 What are the records/entities within this data file? What do they represent?  Imagine this describing what a single row in a CSV represents.
Princeton University Art Museum dataset is available at Github page https://github.com/american-art/PUAM. The dataset includes:

1. Constituents: The constituent data model is saved in multiple formats, including dot, json, md, pdf, ttl, n3. The data set is saved in the format of json. In the dataset (https://github.com/american-art/PUAM/blob/master/apiconstituents_american/apiconstituents_american.json), person (The person may be artist, author, maker, etc of the objects, I need more sources to confirm) information is recorded from the perspective of constituent ID, full display name, alphabetic sort, last name, first name, name title, middle name, suffix, display date, begin data, end date, begin date ISO, end date ISO, nationality, culture group, biography, active (data value is either “1” or “0), approve (data value is either “1” or “0”), system time stamp. 

2. Constituent birth geography: The folder title is “apicongeography_birth”, which means the constituents’ birth geography. The information describes where the constituent was born.  Inside the folder, the data model is saved in the formats of dot, json, md, pdf, ttl, n3 while the data is saved in the format of json at website https://github.com/american-art/PUAM/blob/master/apicongeography_birth/apicongeography.json. The constituent is described by constituent ID, which can be referenced in constituents american folder. The geography information is described from geography ID, geography code (which are all “birth place” in this file), primary display (the data value is either “1” or “0”), continent, sub-continent, country, region, state, city, county, sub-region, locale, locus, river, excavation, latitude, longitude, geoname, system time stamp, U,V, W. 

3. Constituent death geography: The folder title is “apicongeography_death”, which means the constituents’ death geography. The information describes where the constituent died. The data model is saved in the same formats as in the constituent geography birth folder. The geography information is described from geography ID, geography code (which could bel “birth place”, “death place”, or “active place” in this file, by observation, need more coding here), primary display (the data value is either “1” or “0”), continent, sub-continent, country, region, state, city, county, sub-region, locale, locus, river, excavation, latitude, longitude, geoname, system time stamp, U,V, W. 

4. Constituent URI: The folder title is “apiconuris”, which include all the URI of the constituent. The data model is saved in the format of dot, json, md, pdf, ttl, and n3. The data is saved in the format of json. In the data, the information include: constituent ID, Alt Number ID, VIAF (Virtual International Authority File) URI, ULAN ( Getty Union List of Artist Names) URI. 

5. Exhibitions american: The folder title is “apiexhibitions_american”, with only a data file in the format of json. No data model file is inside the folder. The exhibition information is described from the aspects of exhibition ID, exhibition title, display date, begin ISO date, end ISO date, in house (the data value is “0” or “1”), traveling (the data value is “0” or “1”), online history (the data value is “0” or “1”), princeton public (the data value is “0” or “1”), exhibition department, primary image ID, exhibition citation (including title, exhibition area and the according time span), sponsor credit line.

6. Object American: The folder title is “apiobjects_american”, inside which the data model is saved in the formats of dot, json, md, pdf, ttl, jl, and n3. The data is saved in the format of json, which describes the object information. The object information is described from the perspectives of object ID, object number, sort number, dated, date begin, date end, medium (e.g. Gelatin silver prints), dimensions label (the length of the object in centimeter and inch), credit line (e.g, Museum purchase, gift of Merrill Lynch & Co., Inc), restrictions, catrais, edition, department, classification, object status, curator approved (data value is either “1” or “0”).

7. Context reference America: The folder title is “apiobjconxrefs_american” and the folder describes the object and its constituent. The data model is saved in the format of dot, json, md, pdf, ttl, and n3. The data is saved in the format of json, including the fields “context reference id”, “object id”, “display order”, “constituent id”, “role”, prefix, display name (of the constituent), suffix, display bio, concat display, remarks, constatement, displayed (data value is either “0” or “1”).

8. Dimension reference America: The folder title is “”.This folder includes the dimensional information of the object, including dimension type and its URI, dimension unit and its URI, dimension and its URI. The fields include: dimension id (the id of this record), dimension element reference id (e.g. “95636”), object id, element (e.g. overall, sheet), element rank, element description, dimensional type (e.g. width), dimension rank, dimension (e.g. 40.4), dimension unit (e.g. centimeter).

9. Object exhibition reference American: 
9.1 Folder title: apiobjexhxrefs_amrican
9.2 General information: The file include the object and exhibition together, illustrating what objects are displayed in different exhibitions. 
9.3 Files and its structure: No data model files are found in this folder and only one data file, which is saved in the format of json is displayed. 
9.4 Field and/or its meaning and/or an example
9.5 Exhibition object reference id. This field is an ID of a record, describing one object in one exhibition. 
9.6 Object ID
9.7 Exhibition ID
9.8 Exhibition citation. The field summarize the exhibition from exhibition title, display place, exhibition timespan, for example, Painting on Paper: American Watercolors at Princeton: Princeton University Art Museum (27 June 2015 — 30 August 2015).

10. Object geography America
Folder title: apiobjgeograph_american
General information: The file describe where the object was produced.
Files and its structure: The data model is saved in the formats of dot, json, md, pdf, ttl and n3. The data is saved in a json file. 
Field and/or its meaning and/or an example
Object geography ID: the ID of one record, which describes the location where an event (for example, production) happened.
object ID
Geocode: for example, “place dipicted”, “place made”
Primary display: the data value is either “1” or “0”.
Contient, such as North America
Sub-continent
country
region
state
city
county
sub-region
river
locus
excavation
latitude
longtitude
Geonames: The URL of the place on the website https://www.geonames.org/ 

11. Media reference American
Folder title: apiobjmediaxrefs_american
General information: The data describes the information of the object image. 
Files and its structure: The data model is saved in the formats of dot, json, md, pdf, ttl and n3. The data is saved in a json file. 
Field and/or its meaning and/or an example
Expr1: To be checked. The data value of this field is a number, for example, “3832”.
Media reference ID: The ID of the image
Object ID
Media master ID
Media type
Rank: to be checked.
File name
Primary display: The data value is either “1” or “0”.

12. Terms reference American 
Folder title: apiobjtermsxrefs_american 
General information: The data describe the classification, subject and the context of the classification. 
Files and its structure: The data model is saved in the formats of dot, json, md, pdf, ttl and n3. The data is saved in a json file. 
Field and/or its meaning and/or an example
Thes reference ID: This is an ID of an record, which describes one clascification of an object.
Object ID
Thesx reference type: the data value is either “culture”, “subject”, or “classification”. 
AATID: The ID in the Art & Archetecture Thesaurus
Term: 	The culture, subject, or classification of the object.
Entered Date: The data when the information is entered into the system.

13. Title reference american primary titles
Folder title:apiobjtitlexrefs_american_primary_titles
General information:The data describes the primary title information of the objects.
Files and its structure: The data model is saved in the formats of dot, json, md, pdf, ttl and n3. The data is saved in a json file. 
Field and/or its meaning and/or an example
Title ID: The ID of the title
Object ID
Title type: The data value is “primary title” in this file.
Display order: the data value is number, such as “1”, “2”, “3”, “4”. 
Language
Title
Effective ISO date: since when the title started to be effective. The format of the date is in ISO format. 

14. Title reference american unknown titles
Folder title:apiobjtitlexrefs_american_unknown_titles
General information: The data describes the title information of the objects, which might be “unknown”.
Files and its structure: The data model is saved in the formats of dot, json, md, pdf, ttl and n3. The data is saved in a json file. 
Field and/or its meaning and/or an example: The fields are the exactly the same as in the primary title file, however, the title type could be “unknown”.

15. Title reference American other titles
Folder title:apiobjtitlexrefs_american_other_titles
General information: The data describes the title information of the objects, which might be neither “primary title” nor “unknown”, for example, “descriptive title”.
Files and its structure: The data model is saved in the formats of dot, json, md, pdf, ttl and n3. The data is saved in a json file. 
Field and/or its meaning and/or an example: The fields are the exactly the same as in the primary title file, however, the title type could be “descriptive title”.

# 6. Describe the dimensions of the data.  How many records are there? How many properties about each record are there?
## 6.1 Object geography America ( folder title “apiobjects_american”)
1. The number of record: 21730
2. Properties of each record: see my answer to the last question “What are the records/entities within this data file? What do they represent?  Imagine this describing what a single row in a CSV represents.”

## 6.2 What sort of data types are present within the data file?  Describe this in plain human language. For example, integer, categorical, etc.
object ID: interger
object geography ID: interger
geocode: string
continent: string
sub-continent: string
country: string
region: string
state: string
city: string
county: string
sub-region: string
river: string
locus: string
locale: string
latitude: float
longitude: float

# 7. Codebook
## 7.1 Description of column (a short human readable statement of what this column contains).
see my answer to the question: “what are the records/entities within this data file? What do they represent?  Imagine this describing what a single row in a CSV represents.”

## 7.2 Description of data values and units present
Each record includes a object geography ID and an object ID. Geocode tells what type of the place is depicted. I am not sure what primary display represents. The geography information is described from the aspects of continent, sub-continent, country, region, state, city, county, sub-region, river, locus, locale, excavation, latitude, longitude, geoname.

## 7.3 What are all the unique values and their meaning? (if you have categorical data).  Don’t do this if there are more than like 10 or 20.
1. There are 21730 records, and logically speaking, each record should have a object ID and geography object ID. However, there are only 12827 and 12429 unique object geography ID and object ID, which represents some of the geography ID and object ID are repeated. 
2. There are eight types of unique data value for geocode: place depicted (7462), place made (5792), place collected (191), place excavated (173), not assigned (17), geography attribution (7), place located (7), null (8079). I explain why some data value is “null” in my answer to the next question. Geography attribution. “Not assigned” mean the curator cannot find the geography information. For example, the object, the ID of which is 39697, is a photograph taken by Burnham Beeches. There is a tree in the photograph only, thus, there might be no enough information available to the curators to decide where this tree is/was located. “Geography attribution” is similar to “place depicted”, I guess. If necessary, I can email the curator to comfirm. An object, the ID of which is 51450, is a photo of a building in shalow. In the record, the object’s geocode is “geography attribution”, and the data value for country property is “Mexico”. My guess is this is a building in Mexico.
3. Continent: There are some misplaced data value, such as “Australia” should be cleaned. See data cleaning accessment.
4. 20464 out of 21730 of the records have a sub-continent value as “null”.
5. Country: 8151 out of 21730 of the records have a country value as null. For all the other records, there is one country value assigned. 

## 7.4 Reason for missing values and the relevant missing values or codes
Why data value is “null”? There are 8079 records, the geocode value of which is “null”. At the same time, there are 8079 records, the properties of which, are all “null”. It means there are 8079 records out of 21730 records should be deleted. 

## 7.5 Number of known missing values within this column
No missing value is visible, however, several of the records have the data value as “null”.

## 7.6 Other notes, caveats, attribution, etc. that you need to report for this data file.
None

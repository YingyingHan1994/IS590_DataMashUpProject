import pandas as pd
import csv

# Read the file
GM = pd.read_csv("GM_Clean3_CorrectGeographyTerm_withoutDuplicate.csv",encoding = "Latin-1")
#print(GM.shape)

#duplicates = GM.ObjectID.duplicated()

#print(duplicates)

#show = GM.loc[GM.ObjectID.duplicated(keep ='first' ),:]

#print(show)

#print(GM.duplicated(subset=["ObjectID"]).sum())

# Regarding the rows with the same "objectID", keep the first-occured row.
df= GM.drop_duplicates(subset=["ObjectID"])
#print(df)
df.to_csv("GM_clean4_RemoveDuplicate_ObjectID.csv")


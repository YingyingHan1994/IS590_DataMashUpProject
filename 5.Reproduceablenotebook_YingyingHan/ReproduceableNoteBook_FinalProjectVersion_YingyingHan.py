#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd
import csv


# # Read princeton final data file: princeton_clean 12_final version.csv
# # column 1-4 include continent, country, state, city data respectively.

# In[76]:


princeton = pd.read_csv ("princeton_clean 12_final version.csv",encoding = "latin-1")


# # Observation: 
# column 1 is continent data, the column title is "Continent";
# column 2 is country data, the column title is "Country";
# column 3 is state data, the column title is "State";
# column 4 is city data,, the column title is "City"

# # Extract these columns

# In[82]:


princeton_finaldata = princeton.loc[:,["Continent","Country","State","City"]]


# # Write the columns to a csv file: princeton_final

# In[83]:


princeton_finaldata.to_csv("princeton_final.csv")


# # Read GM data file: gm_clean11_finalversion.csv in 

# In[65]:


gm = pd.read_csv ("gm_clean11_finalversion.csv",encoding = "latin-1")


# In[66]:


gm.head()


# # Obeservation on gm data file;
# # city information is in cloumn 3, column title is "name"
# # state informatiion is in column 4, column title is "admin1"
# # country information is in columm 7, column title is "Country"
# # continent information is in column 8, column title is "Continent"

# # Extract the city, state, country, continent information

# In[67]:


gm_finaldata = gm.loc[:,["Continent","Country","admin1","name"]]


# # Write these columns out to a csv file: gm_final.csv. 

# In[59]:


gm_finaldata.to_csv("gm_final.csv")


# # Read saam data file in : saam_clean4_addcontinent.csv 

# In[ ]:





# In[68]:


saam = pd.read_csv ("saam_clean4_addcontinent.csv",encoding = "latin-1")


# In[37]:


saam.head()


# In[ ]:





# In[ ]:





# # Observation: 
# city data is in column 3, the column title is "City"
# 
# state data is in column 5, the column title is "State"
# 
# country data is in column 6, the column title is "Country"
# 
# continent data is in clumn 7, the column title is "Continent"
# 
# 
# 

# # Extract the above-mentioned columns.

# In[69]:


saam_finaldata = saam.loc[:,["Continent","Country","State","City"]]


# 

# # Write the saam data out.

# In[49]:


saam_finaldata.to_csv("saam_final.csv")


# # Merge three files: (1) saam_final.csv; (2) gm_final.csv;(3)princeton_final.csv

# In[84]:


princeton = csv.reader(open("princeton_final.csv"))
gm = csv.reader(open("gm_final.csv"))
saam = csv.reader(open("saam_final.csv"))
f = open("merged_dataset.csv", "w")
writer = csv.writer(f)

for row in princeton:
    writer.writerow(row)
for row in gm:
    writer.writerow(row)
for row in saam:
    writer.writerow(row)
f.close()


# In[ ]:





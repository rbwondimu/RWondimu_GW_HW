#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dependencies
import pandas as pd


# In[ ]:


# load CSV
csv_path = "Resources/2016-FCC-New-Coders-Survey-Data.csv"
new_coder_data = pd.read_csv("Resources/2016-FCC-New-Coders-Survey-Data.csv")
new_coder_data.head()


# In[ ]:


# Read with pandas--low_memory required to suppress errors about mixed data types
cleandata_pd = pd.read_csv(csv_path, encoding = 'iso-8859-1', low_memory=False)
cleandata_pd.head()


# In[ ]:


# Take only columns 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 29, 30, 32, 36, 37, 45, 48, 56, 110, 111
reduced_coders_pd = cleandata_pd.iloc[:, [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 29, 30, 32, 36, 37, 45, 48, 56, 110, 111]]
reduced_coders_pd.head()


# In[ ]:


# Change reading 0 and 1 to No and Yes, respectively
reduced_coders_pd= reduced_coders_pd.replace({0.0: "No", 1.0: "Yes"})
reduced_coders_pd.head()


# In[ ]:


# Extract rows for only those who attended a bootcamp
attended_bootcamp = reduced_coders_pd.loc[reduced_coders_pd["AttendedBootcamp"] == "Yes"]
attended_bootcamp.count()


# In[ ]:


# Create DataFrame of the different boot camps that had a significant number of attendees
bootcamp_name = pd.DataFrame(reduced_coders_pd["BootcampName"].value_counts())

bootcamp_name.reset_index(inplace=True)
bootcamp_name.columns = ["BootcampName", "Count"]


bootcamp_name.head()


# In[ ]:


# Count how many attendees of each bootcamp would recommend the bootcamp
recommend_bootcamp = attended_bootcamp.replace({"Yes": 1, "No": 0})
recommend_bootcamp = pd.DataFrame(recommend_bootcamp.groupby("BootcampName")["BootcampRecommend"].sum())

recommend_bootcamp.reset_index(inplace=True)
recommend_bootcamp.columns=["BootcampName", "Recommenders"]
recommend_bootcamp.head()


# In[ ]:


# Merge the two created data frames on the name of tbe bootcamp
merged_df = pd.merge(bootcamp_name, recommend_bootcamp, on="BootcampName")
merged_df.head()


# In[ ]:


# Calculate percentage of eac bootcamp's students who are recommenders
merged_df["% Recommend"] = merged_df["Recommenders"] / merged_df["Count"] * 100

merged_df = merged_df.sort_values(["% Recommend"], ascending=False).round(2)

merged_df["% Recommend"] = merged_df["% Recommend"].map("{0:,.2f}%".format)

merged_df.head()


# In[ ]:


# Export to excel and remove index
merged_df.to_excel("output/Bootcamppart1B.xlsx", index=False)


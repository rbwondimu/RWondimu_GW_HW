#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np
import random

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

student_df=pd.read_csv(student_data)
school_df=pd.read_csv(school_data)
student_df.head()
school_df.head()

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[ ]:


number_schools = len(school_df["SchoolName"].unique())school_df = school_df.rename(columns={"name":"SchoolName"})
student_df = student_df.rename(columns={"school":"SchoolName"})


# In[ ]:


number_students = school_df["size"].sum()


# In[ ]:


total_budget = school_df["budget"].sum()


# In[ ]:


average_math_score = student_df["math_score"].mean()


# In[ ]:


average_reading_score = student_df["reading_score"].mean()


# In[ ]:


percent_math_pass = ((student_df["math_score"] > 70).sum()/student_df["math_score"].count())*100


# In[ ]:


percent_reading_pass = (((student_df["reading_score"] > 70).sum()/student_df["reading_score"].count())*100)


# In[ ]:


overall_pass = ((percent_math_pass + percent_reading_pass)/2)


# ## School Summary

# In[ ]:


district_summary = pd.DataFrame({"Total Schools":[number_schools],
                               "Total Students":[number_students],
                               "Total Budget" : [total_budget],
                               "Average Math Score":[average_math_score],
                               "Average Reading Score":[average_reading_score],
                               "% Passing Math":[percent_math_pass],
                               "% Passing Reading": [percent_reading_pass],
                               "% Overall Passing Rate":[overall_pass]})

district_summary = district_summary[["Total Schools", "Total Students","Total Budget", "Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing Rate"]]

district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,}".format)
district_summary["Average Math Score"] = district_summary["Average Math Score"].map("{:.2f}%".format)
district_summary["Average Reading Score"] = district_summary["Average Reading Score"].map("{:.2f}%".format)
district_summary["% Passing Math"] = district_summary["% Passing Math"].map("{:.2f}%".format)
district_summary["% Passing Reading"] = district_summary["% Passing Reading"].map("{:.2f}%".format)
district_summary["% Overall Passing Rate"] = district_summary["% Overall Passing Rate"].map("{:.2f}%".format)

district_summary.head()


# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[13]:


sort_school_summary = school_summary.sort_values("% Overall Pass Rate", ascending=False)[:5]
sort_school_summary.head(15)


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[14]:


sort_school_summary = school_summary.sort_values("% Overall Pass Rate")[:5]
sort_school_summary.head(15)


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[ ]:


ninth_df = student_df.loc[student_df["grade"] == "9th"].groupby("SchoolName", as_index=False)
tenth_df = student_df.loc[student_df["grade"] == "10th"].groupby("SchoolName", as_index=False)
eleventh_df = student_df.loc[student_df["grade"] == "11th"].groupby("SchoolName", as_index=False)
twelfth_df = student_df.loc[student_df["grade"] == "12th"].groupby("SchoolName", as_index=False)

ninthM_Avg = pd.DataFrame(ninth_df["math_score"].mean())
tenthM_Avg = pd.DataFrame(tenth_df["math_score"].mean())
eleventhM_Avg = pd.DataFrame(eleventh_df["math_score"].mean())
twelfthM_Avg = pd.DataFrame(twelfth_df["math_score"].mean())

mathByGrade = pd.merge(ninthM_Avg, tenthM_Avg, on="SchoolName")
mathByGrade = pd.merge(mathByGrade, eleventhM_Avg, on="SchoolName")
mathByGrade = pd.merge(mathByGrade, twelfthM_Avg, on="SchoolName")
mathByGrade.columns = ["SchoolName","9th","10th","11th","12th"]
mathByGrade.head(15)


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[16]:


ninthR_Avg = pd.DataFrame(ninth_df["reading_score"].mean())
tenthR_Avg = pd.DataFrame(tenth_df["reading_score"].mean())
eleventhR_Avg = pd.DataFrame(eleventh_df["reading_score"].mean())
twelfthR_Avg = pd.DataFrame(twelfth_df["reading_score"].mean())

readByGrade = pd.merge(ninthR_Avg, tenthR_Avg, on="SchoolName")
readByGrade = pd.merge(readByGrade, eleventhR_Avg, on="SchoolName")
readByGrade = pd.merge(readByGrade, twelfthR_Avg, on="SchoolName")
readByGrade.columns = ["SchoolName","9th","10th","11th","12th"]
readByGrade.head(15)


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[17]:



# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = [“<$585”, “$585-615", “$615-645”, “$645-675"]
scoreByBudget = school_summary_raw[[“Avg Math”, “Avg Reading”, “% Passing Math”, “% Passing Reading”, “% Overall Pass Rate”]].groupby(pd.cut(school_summary_raw[“Budget/Student”], bins=bins, labels=group_names )).mean()
scoreByBudget.head()


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[ ]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = [“Small (<1000)“, “Medium (1000-2000)“, “Large (2000-5000)“]
scoreBySize = school_summary_raw[[“Avg Math”, “Avg Reading”, “% Passing Math”, “% Passing Reading”, “% Overall Pass Rate”]].groupby(pd.cut(school_summary_raw[“Num Students”], bins=bins, labels=group_names)).mean()
scoreBySize.head()


# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[20]:


school_summary_type = school_summary_raw
school_summary_type["Type"] = school_summary_type["Type"].replace({"Charter": 1, "District":2})

bins = [0, 1, 2]
group_names = ["Charter", "District"]
scoreByType = school_summary_type[["Avg Math", "Avg Reading", "% Passing Math", "% Passing Reading", "% Overall Pass Rate"]].groupby(pd.cut(school_summary_type["Type"], bins=bins,labels=group_names)).mean()
scoreByType.head()


# In[ ]:





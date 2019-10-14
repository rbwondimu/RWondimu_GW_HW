#!/usr/bin/env python
# coding: utf-8

# **BIG BIG HINT! Look in the instructions to guide you on this task.**

# In[14]:


# Dependencies
import pandas as pd


# In[15]:


# load CSV
new_coder_data = pd.read_csv("Resources/2016-FCC-New-Coders-Survey-Data.csv")
new_coder_data.head()


# In[16]:


# Inspect all columns
new_coder_data.count()


# In[17]:


# Extract only columns 0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 29, 30, 32, 36, 37, 45, 48, 56, 110, 111
columns = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 29, 30, 32, 36, 37, 45, 48, 56, 110, 111]
extract_new_coder_data = new_coder_data.iloc[columns]
extract_new_coder_data.head()


# In[18]:


#extract_df.AttendedBootcamp.replace(to_replace=[0 ,1], value=['no', 'yes'])
extract_new_coder_data['AttendedBootcamp'] = extract_new_coder_data['AttendedBootcamp'].apply(lambda x: 0 if x=='no' else 1)
extract_new_coder_data.head()


# In[19]:


# Calculate total number of respondents in survey
len(extract_new_coder_data)


# In[21]:


# Extract rows corresponding only to people who attended a bootcamp
extract_new_coder_data=extract_new_coder_data.replace({0.0: "No", 1.0:"Yes"})
extract_new_coder_data.head() 


# In[23]:


# Calculate average age of attendees
aveage_age = extract_new_coder_data["Age"].mean()

# Calculate how many people attended a bootcamp
attended_bootcamp="Total bootcamp attendees"
attended_bootcamp["AttendingBootcamp"].count()

# Calculate how many attendees hold degrees
attended_bootcamp["SchoolDegree"].count()

# Count number of attendees who self-identify as male; female; or are of non-binary gender identification
gender_all = attended_bootcamp["Gender"].count()
male = attended_bootcamp["Gender"].value_counts()["male"]
female = attended_bootcamp["Gender"].value_counts()["female"]
non_binary = gender_all - male - female 

# Calculate percentage of respondents who attended a bootcamp
percent_attended = amount_attended / total_surveyed * 100
# Calculate percentage of respondents belonging to each gender
percent_male = (male / total_gender) * 100
percent_female = (female / total_gender) * 100
percent_non_gender = (non_gender / total_gender) * 100
# Calculate percentage of attendees with a school degree
percent_degree = holds_degree / amount_attended * 100
# Calculate average post-bootcamp salary
avg_salary = attended_bootcamp["BootcampPostSalary"].mean()



# In[ ]:


# Create a new table consolodating above calculations
bootcamp_breakdown = pd.DataFrame({"Total Surveyed":[total_surveyed],
                                  "Total bootcamp attendees":[amount_attended],
                                  "% attended bootcamp":[percent_attended],
                                  "Avg. Age":[average_age],
                                  "% male":[percent_male],
                                  "% female":[percent_female],
                                  "% nonbinary":[percent_non_gender],
                                  "Has a degree":[percent_degree],
                                  "Avg post bootcamp salary":[avg_salary]
                                 })
bootcamp_breakdown = bootcamp_breakdown[["Total Surveyed", "Total bootcamp attendees", "% attended bootcamp", "Avg. Age", "% male", "% female", "% nonbinary", "Has a degree", "Avg post bootcamp salary"]]
bootcamp_breakdown = bootcamp_breakdown.round(2)


# In[ ]:


# Improve formatting before outputting spreadsheet
bootcamp_breakdown["% male"] = bootcamp_breakdown["% male"].map("{0:,.2f}%".format)
bootcamp_breakdown["% female"] = bootcamp_breakdown["% female"].map("{0:,.2f}%".format)
bootcamp_breakdown["% nonbinary"] = bootcamp_breakdown["% nonbinary"].map("{0:,.2f}%".format)
bootcamp_breakdown["% attended bootcamp"] = bootcamp_breakdown["% attended bootcamp"].map("{0:,.2f}%".format)
bootcamp_breakdown["Has a degree"] = bootcamp_breakdown["Has a degree"].map("{0:,.2f}%".format)
bootcamp_breakdown["Avg post bootcamp salary"] = bootcamp_breakdown["Avg post bootcamp salary"].map("{0:,.0f}%".format)


# In[ ]:


# Export to Excel
final_output = summary_new_coder_data.round(2)
final_output.to_excel(‘output/pandas_mini_project_A_output.xlsx’, index=False)


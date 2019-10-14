#!/usr/bin/env python
# coding: utf-8

# # UFO Sightings
# 
# #### The objective of this assignment is for you to explain what is happening in each cell in clear, understandable language. 
# 
# #### _There is no need to code._ The code is there for you, and it already runs. Your task is only to explain what each line in each cell does.
# 
# #### The placeholder cells should describe what happens in the cell below it.

# **Example**: The cell below imports `pandas` as a dependency because `pandas` functions will be used throughout the program, such as the Pandas `DataFrame` as well as the `read_csv` function.

# In[ ]:


import pandas as pd


# # Reads CSV code in the resources folder using Pandas. The prints the first 5 rows using .head 

# In[ ]:


csv_path = "Resources/ufoSightings.csv"

ufo_df = pd.read_csv(csv_path)

ufo_df.head()


# 
# 
# .count returns the frequency of values in ufo dataframe columns. Count of Values could be helpful because it is limited to a single column and returns the frequncy of the values of UFO citings. 
# 
# 

# In[ ]:


ufo_df.count()


# _[Replace this with your clear explanation of what happens in the cell below. What are some pros and cons of using `any` versus `all` as the parameter for `how` in the `dropna()` function?]_
# 
# Using the .dropna to remove a row or column with the paramater how being if "any" NA values are present to drop the row or column. The clean.count will give a total number of values after the dropped rows/ columns 
# Determine if row or column is removed from DataFrame, when we have at least one NA or all NA.
# 
# Alternativly "all" would drop a row or column if all values are NA, instead of just any NA values like "any"
# 

# In[ ]:


clean_ufo_df = ufo_df.dropna(how="any")
clean_ufo_df.count()


# 
# _[Replace this with your clear explanation of what happens in the cell below. Be sure to describe what defining a list of columns and using that as the second parameter in the `loc` function does. Also, which filter was applied and how as well as the expected outcome of applying the filter.]_

# In[ ]:


columns = [
    "datetime",
    "city",
    "state",
    "country",
    "shape",
    "duration (seconds)",
    "duration (hours/min)",
    "comments",
    "date posted"
]

usa_ufo_df = clean_ufo_df.loc[clean_ufo_df["country"] == "us", columns]
usa_ufo_df.head()


# _[Replace this with your clear explanation of what happens in the cell below. Be sure to describe what `value_counts` does as well as why this can be practical. Also, describe what will this return.]_

# In[ ]:


state_counts = usa_ufo_df["state"].value_counts()
state_counts


# _[Replace this with your clear explanation of what happens in the cell below. Be sure to describe what is the data type of `state_counts` and why. Explain why is this step necessary for continuing your analysis.]_
# 
# 

# In[ ]:


state_ufo_counts_df = pd.DataFrame(state_counts)
state_ufo_counts_df.head()


# _[Replace this with your clear explanation of what happens in the cell below. Explain what is being manipulated here, and why would this be more user-friendly to do.]_

# In[ ]:


state_ufo_counts_df = state_ufo_counts_df.rename(
    columns={"state": "Sum of Sightings"})
state_ufo_counts_df.head()


# _[Replace this with your clear explanation of what happens in the cell below. Explain what is happening by calling looking at the `dtypes` property and why this can be helpful.]_

# In[ ]:


usa_ufo_df.dtypes


# _[Replace this with your clear explanation of what happens in the cell below. Be sure to explain why this step is necessary, and what will you now be able to do as a result of performing this step.]_

# In[ ]:


usa_ufo_df.loc[:, "duration (seconds)"] = usa_ufo_df["duration (seconds)"].astype("float")
usa_ufo_df.dtypes


# _[Replace this with your clear explanation of what happens in the cell below. What is the output and how were we able to accomplish this?]_

# In[ ]:


# Now it is possible to find the sum of seconds
usa_ufo_df["duration (seconds)"].sum()


# _[Replace this with your clear explanation of what happens in the cell below. How did we group by two columns, and what are we now able to do as a result? Lastly, explain what does this output tell you.]_

# In[ ]:


grouped_data = usa_ufo_df.groupby(['state', 'city'])

# Hint: If you are counting records, you can use any column and get the same result. Try it.
grouped_data['datetime'].count()


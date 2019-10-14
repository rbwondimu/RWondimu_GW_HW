#!/usr/bin/env python
# coding: utf-8

# # Search For The Worst
# 
# #### The objective of this assignment is for you to explain what is happening in each cell in clear, understandable language. 
# 
# #### _There is no need to code._ The code is there for you, and it already runs. Your task is only to explain what each line in each cell does.
# 
# #### The placeholder cells should describe what happens in the cell below it.

# **Example**: The cell below imports `pandas` as a dependency because `pandas` functions will be used throughout the program, such as the Pandas `DataFrame` as well as the `read_csv` function.

# In[ ]:


import pandas as pd
import numpy as np


# **Example**: The cell below creates a reference to teh csv file and stores it in a variable called `csv_path`. It then creates a DataFrame using the `pd.read_csv` function. The output of the `read_csv` function is a DataFrame.

# In[ ]:


# Create reference to CSV file
csv_path = "Resources/Soccer2018Data.csv"

# Import the CSV into a pandas DataFrame
soccer_2018_df = pd.read_csv(csv_path, low_memory=False)
soccer_2018_df


# # Code is searching Prefered Position column of the dataframe to find unique values to output as a list or array

# In[ ]:


soccer_2018_df["Preferred Position"].unique()


# # New dataframe is being created using preferred position and data on striker. Loc allows for data section based on row and column - based on us setting it  equal to ST - so new dataframe is created by finding values for preferred position of striker. 

# In[ ]:


strikers_2018_df = soccer_2018_df.loc[soccer_2018_df["Preferred Position"] == "ST", :]
strikers_2018_df.head()


# ## Sorting occurs in the dataframe whcih includes players only whose Preferred positoin is Striker. This allows data to be sorted in ascending order from lowest to highest score. Letting you see whoh performed the worst based on identificaiton as a striker. 

# In[ ]:


# Sort the DataFrame by the values in the "ST" column to find the worst
strikers_2018_df = strikers_2018_df.sort_values("ST")

# Reset the index so that the index is now based on the sorting locations
strikers_2018_df = strikers_2018_df.reset_index(drop=True)

strikers_2018_df.head()


# # All the saved worst data function is saved as a varable called worst_striker. Loc set from first row and the colon (:) indicates through all columns of dataframe. And the output is printed for the first row - worst striker data 

# In[ ]:


worst_striker = strikers_2018_df.loc[0, :]
worst_striker


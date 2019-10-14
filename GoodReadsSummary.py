#!/usr/bin/env python
# coding: utf-8

# # Good Reads Summary
# 
# #### The objective of this assignment is for you to explain what is happening in each cell in clear, understandable language. 
# 
# #### _There is no need to code._ The code is there for you, and it already runs. Your task is only to explain what each line in each cell does.
# 
# #### The placeholder cells should describe what happens in the cell below it.

# **Example**: The cell below imports `pandas` as a dependency because `pandas` functions will be used throughout the program, such as the Pandas `DataFrame` as well as the `read_csv` function.

# In[ ]:


import pandas as pd


# The cell uses pandas to read the CSV file. 
# Encoding is necessary because it translates charaacters like letters, punctuations, and symbols to integers / bits that can be sequenced. 
# 

# In[ ]:


goodreads_path = "Resources/books_clean.csv"

goodreads_df = pd.read_csv(goodreads_path, encoding="utf-8")
goodreads_df.head()


# author_count is created which is a variable that finds the total number of authors in the dataset using len() and unique() functions. Then, it finds the earliest and latest publication years using using repsective the min() and max() functions. The iloc function designates an integer based position in the goodreads dataframe from 0 to the length of the axis. The axis setting is important because it specifies the axis along which the means are computed. In this case axis=1 which indicates it's along the columns.
# 

# In[ ]:


author_count = len(goodreads_df["Authors"].unique())

earliest_year = goodreads_df["Publication Year"].min()
latest_year = goodreads_df["Publication Year"].max()

goodreads_df['Total Reviews'] = goodreads_df.iloc[:, 4:].sum(axis=1)
total_reviews = sum(goodreads_df['Total Reviews'])


# A summary table is being created as a Pandas DataFrame representing total unique authors, earliest and latest years, and total reviews. This is being created as a dictionary of lists. The reason author_count needs to be enclosed in square brackets because they designate a list which is mutable and allows you to change it's contents. 

# In[ ]:


summary_table = pd.DataFrame({"Total Unique Authors": [author_count],
                              "Earliest Year": earliest_year,
                              "Latest Year": latest_year,
                              "Total Reviews": total_reviews})
summary_table


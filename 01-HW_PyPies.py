#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


pies = ["Apple", "Pumpkin", "Chocolate Creme", "Cherry", "Apple Crumb",
        "Pecan", "Lemon Meringue", "Blueberry", "Key Lime", "Peach"]
pie_votes = [47, 37, 32, 27, 25, 24, 24, 21, 18, 16]
colors = ["yellow", "green", "lightblue", "orange", "red",
          "purple", "pink", "yellowgreen", "lightskyblue", "lightcoral"]
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)


# In[4]:


# Tell matplotlib to create a pie chart based upon the above data
plt.pie(pie_votes, explode=explode, labels=pies, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
# Create axes which are equal so we have a perfect circle
plt.axis("equal")
# Save an image of our chart and print the final product to the screen
plt.savefig("../Images/PyPies.png")
plt.show()


# In[ ]:





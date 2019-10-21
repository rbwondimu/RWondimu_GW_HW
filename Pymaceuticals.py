#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')
# File to Load (Remember to Change These)
mouse_data_path= os.path.join('data',‘mouse_drug_data.csv')
clinical_data_path = os.path.join(‘data’,‘clinicaltrial_data.csv’)
# Read the Mouse and Drug Data and the Clinical Trial Data
mouse_drug_df = pd.read_csv(mouse_data_path)
clinical_trial_df = pd.read_csv(clinical_data_path)
# Combine the data into a single dataset
complete_df = pd.merge(clinical_trial_df,mouse_drug_df,on=‘Mouse ID’,how=‘left’)
# Display the data table for preview
complete_df.head()


# ## Tumor Response to Treatment

# In[ ]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
grouped_df = complete_df.groupby(['Drug','Timepoint'])['Tumor Volume (mm3)']
avg_tumor_df = grouped_df.mean()

# Convert to DataFrame
avg_tumor_df = avg_tumor_df.reset_index()

# Preview DataFrame
avg_tumor_df.head()


# In[ ]:


# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
tumor_standard_errors = grouped_df.sem()


# Convert to DataFrame
tumor_standard_errors_df = pd.DataFrame(tumor_standard_errors)

# Preview DataFrame
tumor_standard_errors_df.reset_index(inplace=True)
tumor_standard_errors_df.head()


# In[ ]:


# Minor Data Munging to Re-Format the Data Frames
pivot_avg_tumor_df = avg_tumor_df.pivot(index='Timepoint',columns='Drug',values='Tumor Volume (mm3)')

# Preview that Reformatting worked
pivot_avg_tumor_df.head(20)


# In[ ]:


# Generate the Plot (with Error Bars)
# Save the Figure
drug_format_list = [('Capomulin','o','red'),('Infubinol','^','blue'),('Ketapril','s','green'),('Placebo','d','black')]
for drug,marker,colors in drug_format_list:
    ste = tumor_standard_errors[drug]
    tumor_treatment_plt = plt.errorbar(pivot_avg_tumor_df.index,pivot_avg_tumor_df[drug],ste,
                                       fmt=marker,ls='--',color=colors,linewidth=0.5)
plt.legend(loc='best')
plt.title('Tumor Response to Treatment')
plt.xlabel('Time (Days)')
plt.ylabel('Tumor Volume (mm3)')
plt.grid()


# In[ ]:


# Show the Figure
plt.savefig(os.path.join('figures','tumor_response_to_treatment.png'))


# ![Tumor Response to Treatment](../Images/treatment.png)

# ## Metastatic Response to Treatment

# In[ ]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 
grouped_met_df = complete_df.groupby(['Drug','Timepoint'])['Metastatic Sites']
avg_met_df = grouped_met_df.mean()

# Convert to DataFrame
avg_met_df = avg_met_df.reset_index()

# Preview DataFrame
avg_met_df.head()


# In[ ]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 
met_standard_errors = grouped_met_df.sem()

# Convert to DataFrame
met_standard_errors_df = pd.DataFrame(met_standard_errors)

# Preview DataFrame
met_standard_errors_df.reset_index(inplace=True)
met_standard_errors_df.head()


# In[ ]:


# Minor Data Munging to Re-Format the Data Frames
pivot_avg_met_df = avg_met_df.pivot(index='Timepoint',columns='Drug',values='Metastatic Sites')

# Preview that Reformatting worked
pivot_avg_met_df.head(20)


# In[ ]:


# Generate the Plot (with Error Bars)
for drug,marker,colors in drug_format_list:
    ste = met_standard_errors[drug]
    met_treatment_plt = plt.errorbar(pivot_avg_met_df.index,pivot_avg_met_df[drug],ste,
                                       fmt=marker,ls='--',color=colors,linewidth=0.5)

# Show the Figure
plt.legend(loc='best')
plt.title('Metastatic Spread During Treatment')
plt.xlabel('Treatment Duration (Days)')
plt.ylabel('Met. Sites')
plt.grid()

# Save the Figure
plt.savefig(os.path.join('figures','metastic_spread_during_treatment.png'))


# ![Metastatic Spread During Treatment](../Images/spread.png)

# ## Survival Rates

# In[ ]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
mouse_grouped_df = complete_df.groupby(['Drug','Timepoint'])['Mouse ID']
count_mouse_df = mouse_grouped_df.nunique()
count_mouse_df = pd.DataFrame(count_mouse_df)

# Convert to DataFrame
count_mouse_df.reset_index(inplace=True)
count_mouse_df=count_mouse_df.rename(columns={'Mouse ID':'Mouse Count'})

# Preview DataFrame
count_mouse_df.head()


# In[ ]:


# Minor Data Munging to Re-Format the Data Frames
pivot_count_mouse_df = count_mouse_df.pivot(index='Timepoint',columns='Drug',values='Mouse Count')

# Preview the Data Frame
pivot_count_mouse_df.head()


# In[ ]:


# Generate the Plot (Accounting for percentages)
for drug,marker,colors in drug_format_list:
    total_mouse = pivot_count_mouse_df[drug][0]
    survival_rate = (pivot_count_mouse_df[drug]/total_mouse)*100
    survival_treatment_plt = plt.plot(pivot_count_mouse_df.index,survival_rate,
                                       marker=marker,ls='--',color=colors,linewidth=0.5)

# Show the Figure
plt.legend(loc='best')
plt.title('Survival During Treatment')
plt.xlabel('Times (Days)')
plt.ylabel('Survival Rate (%)')
plt.grid()

# Save the Figure
plt.savefig(os.path.join('figures','survival_during_treatment.png'))


# ![Metastatic Spread During Treatment](../Images/survival.png)

# ## Summary Bar Graph

# In[ ]:


# Calculate the percent changes for each drug
percentage_change = (pivot_avg_tumor_df.iloc[-1]/(pivot_avg_tumor_df.iloc[0])-1)*100

# Display the data to confirm
percentage_change


# In[ ]:


# Splice the data between passing and failing drugs
passing = percentage_change < 0

# Orient widths. Add labels, tick marks, etc. 
drug_list = ['Capomulin','Infubinol','Ketapril','Placebo']
change_list = [(percentage_change[durg])for durg in drug_list]
change_plt = plt.bar(drug_list,change_list,width=-1,align='edge',color=passing.map({True:'g',False:'r'}))
plt.grid()
plt.ylim(-30,70)
plt.ylabel('% Tumor Volume Change')
plt.title('Tumor Change over 45 Day Treatment')

# Use functions to label the percentages of changes
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 0:
            label_position = 2
        else:
            label_position = -8
        plt.text(rect.get_x() + rect.get_width()/2., label_position,
                '%d' % int(height)+'%',color='white',
                ha='center', va='bottom')
                
# Call functions to implement the function calls
autolabel(change_plt)

# Save the Figure
plt.savefig(os.path.join('figures','tumor_change_over_45day_treatment.png'))

# Show the Figure
fig.show()


# ![Metastatic Spread During Treatment](../Images/change.png)

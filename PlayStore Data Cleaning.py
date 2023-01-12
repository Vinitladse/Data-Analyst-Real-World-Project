#!/usr/bin/env python
# coding: utf-8

# ## MODULE 1  : Cleaning Data and irrelavent Values By StoryTellers (Vinit Ladse)

# #### importing the required libraries

# In[75]:


import pandas as pd #dataframe manipulation
import numpy as np #statistical manipulations
import os #directory 


# #### Importing Data

# In[76]:


os.chdir('C:\\Users\\Madjid\\Desktop\\Competition\\playstoreliveproj') #specifying the direcotory where there is all the file
df = pd.read_csv('playstore_apps.csv') #reading  and stroing the data
df2 = pd.read_csv('playstore_reviews.csv')


# #### Viewing the Data

# In[77]:


df.head()


# In[78]:


df2.head()


# #### Checking duplicates using .duplicated() method

# In[80]:


#checking for duplicates
df[df['App'].duplicated()==True]


# #### removing them

# In[81]:


#removing duplicates
df.drop_duplicates(["App"],inplace=True,keep='first')


# In[82]:


#making sure duplicares are removed
df[df['App'].duplicated()==True]


# #### function to iterate through columns and return unique values

# In[83]:


#checking the uniques + removing irrelavent parts  
#checking duplicates and removing duplicates 
def checkforuniques(df) :
    for i in df.columns :
        print(f'this is {i} unique values')
        display(df[i].unique())


# In[84]:


checkforuniques(df)


# In[43]:


checkforuniques(df2)


# #### function to check the irrelavent values

# In[85]:


#checking the irrelavent values and deciding if we should remove them 
def checkirrelav(df,col,unique) :
    display(df[df[col]==unique])


# In[96]:


checkirrelav(df,'Category','1.9')


# In[97]:


checkirrelav(df,'Rating',19) #same previuos column , we need to remove this 


# #### removing the irrelavant value

# In[95]:


df =df[df['Category'] !='1.9']


# #### Exporting the results into the same Directory 

# In[98]:


df.to_csv('Cleaned_playstoreApps.csv')
df2.to_csv('CleanedReviews.csv')


# #### The next step is to handle missing values in Excel(by Shruti Sharma) 

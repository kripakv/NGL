#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# In[3]:


data=pd.read_csv('C:/browser_rankings_data.csv')
data.head()


# In[4]:


data.shape


# In[5]:


data.columns


# In[6]:


data.isnull().sum()


# In[7]:


plt.scatter('keyword','browser_rankings')


# In[8]:


from scipy.stats import norm


# In[9]:


data.head(10)


# In[10]:


plt.scatter('keyword','Rank')


# In[11]:


import seaborn as sns


# ## To understand whether correlation between Keyword, Rank,browser_rankings

# In[28]:


df = pd.DataFrame(data,columns=['Keyword','Rank','browser_rankings'])
corrMatrix = df.corr()
print (corrMatrix)


# In[29]:


sns.heatmap(corrMatrix, annot=True)
plt.show()


# ## We found no correlation between these 3 variables

# ## To check whether any correlation between Short Description,Long Description&Ranking 

# In[35]:


df = pd.DataFrame(data,columns=['Short Description','Rank','Long Description'])
corrMatrix = df.corr()
print (corrMatrix)


# In[36]:


sns.heatmap(corrMatrix, annot=True)
plt.show()


# ## We found very small correlation in Long Description

# ## To check whether there any correlation between AppID and Rank

# In[37]:


df = pd.DataFrame(data,columns=['App ID','Rank'])
corrMatrix = df.corr()
print (corrMatrix)


# In[38]:


sns.heatmap(corrMatrix, annot=True)
plt.show()


# In[43]:


import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)


# In[44]:


df = pd.DataFrame(data,columns=['App ID','Rank'])
df.iplot(kind='box')


# In[45]:


df = pd.DataFrame(data,columns=['App ID','Rank'])
df.iplot()


# In[46]:


df.iplot(kind='surface',colorscale='rdylbu')


# In[50]:


df = pd.DataFrame(data,columns=['App ID','Rank'])
df.plot(kind='hist')


# In[54]:


df = pd.DataFrame(data,columns=['App ID','Rank'])
df.plot(kind='bar')


# ## No correlation between AppID & Rank

# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np


# In[14]:


get_ipython().system('pip install textblob_fr ')


# In[15]:


from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import re
import string
from textblob import TextBlob


# In[16]:


data = pd.read_csv('C:/chrome_reviews.csv')
data.head()


# In[17]:


data.shape


# In[18]:


data.columns


# In[19]:


data.isnull().sum()


# In[20]:


data= data.drop(['User Name'],axis=1)
data= data.drop(['Developer Reply'],axis=1)
data= data.drop(['Version'],axis=1)
data= data.drop(['Review URL'],axis=1)
data= data.drop(['Review Date'],axis=1)
data= data.drop(['App ID'],axis=1)
data.head()


# In[23]:


data.dropna(inplace=True)


# In[24]:


data.isnull().sum()


# In[26]:


data.head(10)


# In[27]:


data = data[data.Star != 5]
data = data[data.Star != 4]
data = data[data.Star != 3]
data.head()


# In[28]:


senti_list = []
for i in data["Text"]:
    score = TextBlob(i).sentiment[0]
    if (score > 0):
        senti_list.append('Positive')
    elif (score < 0):
        senti_list.append('Negative')
    else:
        senti_list.append('Neutral') 


# In[29]:


data["sentiment"]=senti_list
data.head()


# In[37]:


data = data[data.sentiment == 'Positive']
data.head(10)


# In[38]:


data.to_csv(r'C:\Users\kripa\OneDrive\Documents\datanew.csv',index=False)


# In[ ]:





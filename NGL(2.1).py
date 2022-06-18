#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import re
import string
from textblob import TextBlob


# In[3]:


data=pd.read_csv('C:/review_data.csv')
data.head()


# In[16]:


data.drop(['star','app_id','reviewDate'],inplace=True,axis=1)


# In[18]:


data.head()


# In[26]:


t=data['text']
t


# In[29]:


t[0]


# In[30]:


t1=TextBlob(t[0])


# In[31]:


print(t1.correct())


# In[33]:


data.head(20)


# In[34]:


t[16]


# In[35]:


t2=TextBlob(t[16])


# In[36]:


print(t2.correct())


# In[39]:


data.tail(20)


# In[40]:


t[29983]


# In[41]:


t3=TextBlob(t[29983])


# In[42]:


print(t3.correct())


# In[45]:


t4=t.iloc[0:2999]


# In[46]:


t4


# ### Not able to TextBlob.correct the full dataset . It's showing some errors.

# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Part1

# ## Question 1

# In[1]:


#Write a regex to extract all the numbers with orange color background from the below text in italics.


#{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}


# In[14]:


get_ipython().system('pip install pillow')


# In[15]:


from PIL import Image


# In[16]:


im=Image.open('C:\Dict_img.png')


# In[17]:


display(im)


# In[18]:


import pandas as pd


# In[19]:


jsn={"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}


# In[20]:


l = pd.json_normalize(jsn['orders'])['id'].tolist() 


# In[21]:


l


# In[22]:


m=pd.json_normalize(jsn['errors'])['code'].tolist()


# In[23]:


m


# In[24]:


k=l+m


# In[25]:


k


# In[ ]:





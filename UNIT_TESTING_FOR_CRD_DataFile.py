#!/usr/bin/env python
# coding: utf-8

# ### Importing the main FreshWorks_CRDpy1 python file as a pakage as fw for testing
# 
# 

# In[11]:


import FreshWorks_CRDpy1 as fw


# ### Performing testing for Create, Read and Delete opearations on the datafile.

# In[8]:


fw.DataFile_Creation("AppleInc",35)


# In[13]:


fw.DataFile_Creation("Mumbai",65)
#will throw an error as key given already present in datastore


# In[14]:


fw.DataFile_Creation("Samsung",100)


# In[21]:


fw.DataFile_Creation("Pakage",120000000)


# In[22]:


fw.DataFile_Creation("PakageIs",550000)


# ### For Reading the Key object abd returning its Value if present in the DataStore.

# In[25]:


fw.DataFile_Read("Freshworks")


# In[26]:


fw.DataFile_Read("Chennai")


# In[29]:


fw.DataFile_Read("Delhi")
# This will throw an error as no such key is present and will not able to read from DataStore 


# In[30]:


fw.DataFile_Read("Jobs")


# ### For Deleting a key from the existing DataFile

# In[31]:


fw.DataFile_Deletion("Samsung")


# In[34]:


fw.DataFile_Deletion("Kolkata")

#This will throw an error as Kolkata named key does not exist in the DataFile Created. 


# In[36]:


fw.DataFile_Deletion("Microsoft")

#This will throw an error as time limit has expired as in given value parameters of this key as(time.time()>z[1])


# In[37]:


fw.DataFile_Deletion("Deloitte")


# In[ ]:





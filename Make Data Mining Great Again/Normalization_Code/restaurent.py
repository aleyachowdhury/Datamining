
# coding: utf-8

# In[1]:

import pandas as pd


# In[3]:

df= pd.read_csv("RESTAURANTS.csv")


# In[4]:

df


# In[5]:

df['FFR07']= (df['FFR07'].values- df['FFR07'].min())/ (df['FFR07'].max()- df['FFR07'].min())


# In[6]:

df['FFR12']= (df['FFR12'].values- df['FFR12'].min())/ (df['FFR12'].max()- df['FFR12'].min())


# In[7]:

df['PCH_FFR_07_12']= (df['PCH_FFR_07_12'].values- df['PCH_FFR_07_12'].min())/ (df['PCH_FFR_07_12'].max()- df['PCH_FFR_07_12'].min())


# In[9]:

df['FFRPTH07']= (df['FFRPTH07'].values- df['FFRPTH07'].min())/ (df['FFRPTH07'].max()- df['FFRPTH07'].min())


# In[10]:

df['FFRPTH12']= (df['FFRPTH12'].values- df['FFRPTH12'].min())/ (df['FFRPTH12'].max()- df['FFRPTH12'].min())


# In[11]:

df['PCH_FFRPTH_07_12']= (df['PCH_FFRPTH_07_12'].values- df['PCH_FFRPTH_07_12'].min())/ (df['PCH_FFRPTH_07_12'].max()- df['PCH_FFRPTH_07_12'].min())


# In[12]:

df['FSR07']= (df['FSR07'].values- df['FSR07'].min())/ (df['FSR07'].max()- df['FSR07'].min())


# In[13]:

df['FSR12']= (df['FSR12'].values- df['FSR12'].min())/ (df['FSR12'].max()- df['FSR12'].min())


# In[14]:

df['PCH_FSR_07_12']= (df['PCH_FSR_07_12'].values- df['PCH_FSR_07_12'].min())/ (df['PCH_FSR_07_12'].max()- df['PCH_FSR_07_12'].min())


# In[15]:

del df['PC_FFRSALES02']


# In[18]:

del df['PC_FSRSALES02']


# In[20]:

del df['PC_FSRSALES07']


# In[22]:

df.to_csv('RESTAURANTS.csv')


# In[ ]:




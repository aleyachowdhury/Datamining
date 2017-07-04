
# coding: utf-8

# In[23]:

import pandas as pd


# In[24]:

df=pd.read_csv("ACCESS.csv")


# In[25]:

df


# In[26]:

df['LACCESS_POP10']= (df['LACCESS_POP10'].values- df['LACCESS_POP10'].min())/ (df['LACCESS_POP10'].max()- df['LACCESS_POP10'].min())


# In[27]:

df['PCT_LACCESS_POP10']= (df['PCT_LACCESS_POP10'].values- df['PCT_LACCESS_POP10'].min())/ (df['PCT_LACCESS_POP10'].max()- df['PCT_LACCESS_POP10'].min())


# In[28]:

df['LACCESS_LOWI10']= (df['LACCESS_LOWI10'].values- df['LACCESS_LOWI10'].min())/ (df['LACCESS_LOWI10'].max()- df['LACCESS_LOWI10'].min())


# In[29]:

df['PCT_LACCESS_LOWI10']= (df['PCT_LACCESS_LOWI10'].values- df['PCT_LACCESS_LOWI10'].min())/ (df['PCT_LACCESS_LOWI10'].max()- df['PCT_LACCESS_LOWI10'].min())


# In[30]:

df['LACCESS_CHILD10']= (df['LACCESS_CHILD10'].values- df['LACCESS_CHILD10'].min())/ (df['LACCESS_CHILD10'].max()- df['LACCESS_CHILD10'].min())


# In[31]:

df['PCT_LACCESS_CHILD10']= (df['PCT_LACCESS_CHILD10'].values- df['PCT_LACCESS_CHILD10'].min())/ (df['PCT_LACCESS_CHILD10'].max()- df['PCT_LACCESS_CHILD10'].min())


# In[32]:

df['LACCESS_SENIORS10']= (df['LACCESS_SENIORS10'].values- df['LACCESS_SENIORS10'].min())/ (df['LACCESS_SENIORS10'].max()- df['LACCESS_SENIORS10'].min())


# In[33]:

df['PCT_LACCESS_SENIORS10']= (df['PCT_LACCESS_SENIORS10'].values- df['PCT_LACCESS_SENIORS10'].min())/ (df['PCT_LACCESS_SENIORS10'].max()- df['PCT_LACCESS_SENIORS10'].min())


# In[34]:

df['LACCESS_HHNV10']= (df['LACCESS_HHNV10'].values- df['LACCESS_HHNV10'].min())/ (df['LACCESS_HHNV10'].max()- df['LACCESS_HHNV10'].min())


# In[35]:

df['PCT_LACCESS_HHNV10']= (df['PCT_LACCESS_HHNV10'].values- df['PCT_LACCESS_HHNV10'].min())/ (df['PCT_LACCESS_HHNV10'].max()- df['PCT_LACCESS_HHNV10'].min())


# In[36]:

df.to_csv('ACCESS.csv')


# In[ ]:




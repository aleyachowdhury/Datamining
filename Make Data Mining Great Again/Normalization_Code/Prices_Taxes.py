
# coding: utf-8

# In[3]:

import pandas as pd


# In[5]:

df=pd.read_csv("PRICES_TAXES.csv")


# In[10]:

df['MILK_PRICE10']= (df['MILK_PRICE10'].values- df['MILK_PRICE10'].min())/ (df['MILK_PRICE10'].max()- df['MILK_PRICE10'].min())


# In[11]:

df['SODA_PRICE10']= (df['SODA_PRICE10'].values- df['SODA_PRICE10'].min())/ (df['SODA_PRICE10'].max()- df['SODA_PRICE10'].min())


# In[12]:

df['MILK_SODA_PRICE10']= (df['MILK_SODA_PRICE10'].values- df['MILK_SODA_PRICE10'].min())/ (df['SODA_PRICE10'].max()- df['MILK_SODA_PRICE10'].min())


# In[13]:

del df['SODATAX_STORES11']


# In[14]:

del df['SODATAX_VENDM11']


# In[15]:

del df['CHIPSTAX_STORES11']


# In[16]:

del df['CHIPSTAX_VENDM11']


# In[17]:

del df['FOOD_TAX11']


# In[21]:

df.to_csv('PRICES_TAXES.csv')


# In[ ]:





# coding: utf-8

# In[137]:

import pandas as pd
import numpy as np


# In[153]:

df= pd.read_csv("HEALTH.csv")
df


# In[139]:

df['PCT_DIABETES_ADULTS09']= (df['PCT_DIABETES_ADULTS09'].values- df['PCT_DIABETES_ADULTS09'].min())/ (df['PCT_DIABETES_ADULTS09'].max()- df['PCT_DIABETES_ADULTS09'].min())


# In[140]:

df['PCT_DIABETES_ADULTS10']= (df['PCT_DIABETES_ADULTS10'].values- df['PCT_DIABETES_ADULTS10'].min())/ (df['PCT_DIABETES_ADULTS10'].max()- df['PCT_DIABETES_ADULTS10'].min())


# In[141]:

df['PCT_OBESE_ADULTS09']= (df['PCT_OBESE_ADULTS09'].values- df['PCT_OBESE_ADULTS09'].min())/ (df['PCT_OBESE_ADULTS09'].max()- df['PCT_OBESE_ADULTS09'].min())


# In[142]:

df['PCT_OBESE_ADULTS10']= (df['PCT_OBESE_ADULTS10'].values- df['PCT_OBESE_ADULTS10'].min())/ (df['PCT_OBESE_ADULTS10'].max()- df['PCT_OBESE_ADULTS10'].min())


# In[143]:

df['PCT_OBESE_CHILD08']= (df['PCT_OBESE_CHILD08'].values- df['PCT_OBESE_CHILD08'].min())/ (df['PCT_OBESE_CHILD08'].max()- df['PCT_OBESE_CHILD08'].min())


# In[144]:

df['PCT_OBESE_CHILD11']= (df['PCT_OBESE_CHILD11'].values- df['PCT_OBESE_CHILD11'].min())/ (df['PCT_OBESE_CHILD11'].max()- df['PCT_OBESE_CHILD11'].min())


# In[145]:

df['PCH_OBESE_CHILD_08_11']= (df['PCH_OBESE_CHILD_08_11'].values- df['PCH_OBESE_CHILD_08_11'].min())/ (df['PCH_OBESE_CHILD_08_11'].max()- df['PCH_OBESE_CHILD_08_11'].min())


# In[146]:

df['RECFAC07']= (df['RECFAC07'].values- df['RECFAC07'].min())/ (df['RECFAC07'].max()- df['RECFAC07'].min())


# In[147]:

df['RECFAC12']= (df['RECFAC12'].values- df['RECFAC12'].min())/ (df['RECFAC12'].max()- df['RECFAC12'].min())


# In[148]:

df['NATAMEN']= (df['NATAMEN'].values- df['NATAMEN'].min())/ (df['NATAMEN'].max()- df['NATAMEN'].min())


# In[152]:

del df['PCT_HSPA09']


# In[ ]:

del df['PCT_OBESE_ADULTS13']


# In[ ]:

df.to_csv('HEALTH.csv')


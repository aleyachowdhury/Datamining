
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df=pd.read_csv("STORES.csv")


# In[3]:

df


# In[4]:

df['GROC07']= (df['GROC07'].values- df['GROC07'].min())/ (df['GROC07'].max()- df['GROC07'].min())


# In[5]:

df['GROC12']= (df['GROC12'].values- df['GROC12'].min())/ (df['GROC12'].max()- df['GROC12'].min())


# In[6]:

df['PCH_GROC_07_12']= (df['PCH_GROC_07_12'].values- df['PCH_GROC_07_12'].min())/ (df['PCH_GROC_07_12'].max()- df['PCH_GROC_07_12'].min())


# In[7]:

df['GROCPTH07']= (df['GROCPTH07'].values- df['GROCPTH07'].min())/ (df['GROCPTH07'].max()- df['GROCPTH07'].min())


# In[10]:

df['PCH_GROCPTH_07_12']= (df['PCH_GROCPTH_07_12'].values- df['PCH_GROCPTH_07_12'].min())/ (df['PCH_GROCPTH_07_12'].max()- df['PCH_GROCPTH_07_12'].min())


# In[11]:

df['GROCPTH12']= (df['GROCPTH12'].values- df['GROCPTH12'].min())/ (df['GROCPTH12'].max()- df['GROCPTH12'].min())


# In[13]:

df['SUPERC07']= (df['SUPERC07'].values- df['SUPERC07'].min())/ (df['SUPERC07'].max()- df['SUPERC07'].min())


# In[14]:

df['PCH_SNAPS_08_12']= (df['PCH_SNAPS_08_12'].values- df['PCH_SNAPS_08_12'].min())/ (df['PCH_SNAPS_08_12'].max()- df['PCH_SNAPS_08_12'].min())


# In[16]:

df['SNAPSPTH08']= (df['SNAPSPTH08'].values- df['SNAPSPTH08'].min())/ (df['SNAPSPTH08'].max()- df['SNAPSPTH08'].min())


# In[17]:

df['SNAPSPTH12']= (df['SNAPSPTH12'].values- df['SNAPSPTH12'].min())/ (df['SNAPSPTH12'].max()- df['SNAPSPTH12'].min())


# In[18]:

df['PCH_SNAPSPTH_08_12']= (df['PCH_SNAPSPTH_08_12'].values- df['PCH_SNAPSPTH_08_12'].min())/ (df['PCH_SNAPSPTH_08_12'].max()- df['PCH_SNAPSPTH_08_12'].min())


# In[19]:

df['WICS08']= (df['WICS08'].values- df['WICS08'].min())/ (df['WICS08'].max()- df['WICS08'].min())


# In[20]:

df['WICS12']= (df['WICS12'].values- df['WICS12'].min())/ (df['WICS12'].max()- df['WICS12'].min())


# In[21]:

df['PCH_WICS_08_12']= (df['PCH_WICS_08_12'].values- df['PCH_WICS_08_12'].min())/ (df['PCH_WICS_08_12'].max()- df['PCH_WICS_08_12'].min())


# In[22]:

df['WICSPTH08']= (df['WICSPTH08'].values- df['WICSPTH08'].min())/ (df['WICSPTH08'].max()- df['WICSPTH08'].min())


# In[23]:

df['WICSPTH12']= (df['WICSPTH12'].values- df['WICSPTH12'].min())/ (df['WICSPTH12'].max()- df['WICSPTH12'].min())


# In[24]:

df['PCH_WICSPTH_08_12']= (df['PCH_WICSPTH_08_12'].values- df['PCH_WICSPTH_08_12'].min())/ (df['PCH_WICSPTH_08_12'].max()- df['PCH_WICSPTH_08_12'].min())


# In[26]:

df.to_csv('STORES.csv')


# In[27]:

df['SUPERC12']= (df['SUPERC12'].values- df['SUPERC12'].min())/ (df['SUPERC12'].max()- df['SUPERC12'].min())


# In[28]:

df['PCH_SUPERC_07_12']= (df['PCH_SUPERC_07_12'].values- df['PCH_SUPERC_07_12'].min())/ (df['PCH_SUPERC_07_12'].max()- df['PCH_SUPERC_07_12'].min())


# In[29]:

df['SUPERCPTH07']= (df['SUPERCPTH07'].values- df['SUPERCPTH07'].min())/ (df['SUPERCPTH07'].max()- df['SUPERCPTH07'].min())


# In[30]:

df['SUPERCPTH12']= (df['SUPERCPTH12'].values- df['SUPERCPTH12'].min())/ (df['SUPERCPTH12'].max()- df['SUPERCPTH12'].min())


# In[31]:

df['PCH_SUPERCPTH_07_12']= (df['PCH_SUPERCPTH_07_12'].values- df['PCH_SUPERCPTH_07_12'].min())/ (df['PCH_SUPERCPTH_07_12'].max()- df['PCH_SUPERCPTH_07_12'].min())


# In[32]:

df['CONVS07']= (df['CONVS07'].values- df['CONVS07'].min())/ (df['CONVS07'].max()- df['CONVS07'].min())


# In[33]:

df['CONVS12']= (df['CONVS12'].values- df['CONVS12'].min())/ (df['CONVS12'].max()- df['CONVS12'].min())


# In[34]:

df['PCH_CONVS_07_12']= (df['PCH_CONVS_07_12'].values- df['PCH_CONVS_07_12'].min())/ (df['PCH_CONVS_07_12'].max()- df['PCH_CONVS_07_12'].min())


# In[35]:

df['CONVSPTH07']= (df['CONVSPTH07'].values- df['CONVSPTH07'].min())/ (df['CONVSPTH07'].max()- df['CONVSPTH07'].min())


# In[36]:

df['CONVSPTH12']= (df['CONVSPTH12'].values- df['CONVSPTH12'].min())/ (df['CONVSPTH12'].max()- df['CONVSPTH12'].min())


# In[37]:

df['PCH_CONVSPTH_07_12']= (df['PCH_CONVSPTH_07_12'].values- df['PCH_CONVSPTH_07_12'].min())/ (df['PCH_CONVSPTH_07_12'].max()- df['PCH_CONVSPTH_07_12'].min())


# In[38]:

df['SPECS07']= (df['SPECS07'].values- df['SPECS07'].min())/ (df['SPECS07'].max()- df['SPECS07'].min())


# In[39]:

df['SPECS12']= (df['SPECS12'].values- df['SPECS12'].min())/ (df['SPECS12'].max()- df['SPECS12'].min())


# In[40]:

df['PCH_SPECS_07_12']= (df['PCH_SPECS_07_12'].values- df['PCH_SPECS_07_12'].min())/ (df['PCH_SPECS_07_12'].max()- df['PCH_SPECS_07_12'].min())


# In[41]:

df['SPECSPTH07']= (df['SPECSPTH07'].values- df['SPECSPTH07'].min())/ (df['SPECSPTH07'].max()- df['SPECSPTH07'].min())


# In[42]:

df['SPECSPTH12']= (df['SPECSPTH12'].values- df['SPECSPTH12'].min())/ (df['SPECSPTH12'].max()- df['SPECSPTH12'].min())


# In[43]:

df['PCH_SPECSPTH_07_12']= (df['PCH_SPECSPTH_07_12'].values- df['PCH_SPECSPTH_07_12'].min())/ (df['PCH_SPECSPTH_07_12'].max()- df['PCH_SPECSPTH_07_12'].min())


# In[44]:

df['SNAPS08']= (df['SNAPS08'].values- df['SNAPS08'].min())/ (df['SNAPS08'].max()- df['SNAPS08'].min())


# In[45]:

df['SNAPS12']= (df['SNAPS12'].values- df['SNAPS12'].min())/ (df['SNAPS12'].max()- df['SNAPS12'].min())


# In[46]:

df.to_csv('STORES.csv')


# In[ ]:




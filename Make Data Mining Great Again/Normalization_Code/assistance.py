
# coding: utf-8

# In[23]:

import pandas as pd


# In[26]:

df=pd.read_csv("ASSISTANCE.csv")


# In[27]:

df


# In[28]:

df['REDEMP_SNAPS08']= (df['REDEMP_SNAPS08'].values- df['REDEMP_SNAPS08'].min())/ (df['REDEMP_SNAPS08'].max()- df['REDEMP_SNAPS08'].min())



# In[29]:

df['REDEMP_SNAPS12']= (df['REDEMP_SNAPS12'].values- df['REDEMP_SNAPS12'].min())/ (df['REDEMP_SNAPS12'].max()- df['REDEMP_SNAPS12'].min())



# In[30]:

df['PCH_REDEMP_SNAPS_08_12']= (df['PCH_REDEMP_SNAPS_08_12'].values- df['PCH_REDEMP_SNAPS_08_12'].min())/ (df['PCH_REDEMP_SNAPS_08_12'].max()- df['PCH_REDEMP_SNAPS_08_12'].min())



# In[37]:

del df['PCT_SNAP09']


# In[38]:

del df['PCT_SNAP14']


# In[39]:

del df['PCH_SNAP_09_14']


# In[40]:

df['PC_SNAPBEN08']= (df['PC_SNAPBEN08'].values- df['PC_SNAPBEN08'].min())/ (df['PC_SNAPBEN08'].max()- df['PC_SNAPBEN08'].min())



# In[41]:

df['PC_SNAPBEN10']= (df['PC_SNAPBEN10'].values- df['PC_SNAPBEN10'].min())/ (df['PC_SNAPBEN10'].max()- df['PC_SNAPBEN10'].min())



# In[42]:

df['PCH_PC_SNAPBEN_08_10']= (df['PCH_PC_SNAPBEN_08_10'].values- df['PCH_PC_SNAPBEN_08_10'].min())/ (df['PCH_PC_SNAPBEN_08_10'].max()- df['PCH_PC_SNAPBEN_08_10'].min())



# In[43]:

del df['SNAP_PART_RATE08']


# In[44]:

del df['SNAP_PART_RATE10']


# In[45]:

del df['SNAP_OAPP00']


# In[46]:

del df['SNAP_OAPP05']


# In[47]:

del df['SNAP_OAPP10']


# In[49]:

del df['SNAP_FACEWAIVER00']


# In[51]:

del df['SNAP_FACEWAIVER05']


# In[52]:

del df['SNAP_VEHEXCL00']


# In[53]:

del df['SNAP_VEHEXCL05']


# In[54]:

del df['SNAP_VEHEXCL10']


# In[55]:

del df['SNAP_BBCE00']


# In[56]:

del df['SNAP_BBCE05']


# In[58]:

df['PCT_FREE_LUNCH06']= (df['PCT_FREE_LUNCH06'].values- df['PCT_FREE_LUNCH06'].min())/ (df['PCT_FREE_LUNCH06'].max()- df['PCT_FREE_LUNCH06'].min())



# In[59]:

df['PCT_FREE_LUNCH10']= (df['PCT_FREE_LUNCH10'].values- df['PCT_FREE_LUNCH10'].min())/ (df['PCT_FREE_LUNCH10'].max()- df['PCT_FREE_LUNCH10'].min())



# In[60]:

df['PCT_REDUCED_LUNCH06']= (df['PCT_REDUCED_LUNCH06'].values- df['PCT_REDUCED_LUNCH06'].min())/ (df['PCT_REDUCED_LUNCH06'].max()- df['PCT_REDUCED_LUNCH06'].min())



# In[61]:

df['PCT_REDUCED_LUNCH10']= (df['PCT_REDUCED_LUNCH10'].values- df['PCT_REDUCED_LUNCH10'].min())/ (df['PCT_REDUCED_LUNCH06'].max()- df['PCT_REDUCED_LUNCH10'].min())



# In[62]:

df['PC_WIC_REDEMP08']= (df['PC_WIC_REDEMP08'].values- df['PC_WIC_REDEMP08'].min())/ (df['PC_WIC_REDEMP08'].max()- df['PC_WIC_REDEMP08'].min())



# In[64]:

df.to_csv('ASSISTANCE.csv')


# In[65]:

df


# In[ ]:




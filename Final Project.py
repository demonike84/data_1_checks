#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install matplotlib
# pip install pandas
# pip install numpy
# pip install openpyxl


# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
Receiving = pd.read_excel('assets/Receiving.xlsx', sheet_name = 'Receiving_Data')
Receivers = (Receiving['Name'].unique())

print(Receivers)


# In[3]:


Receiver = Receiving[Receiving['Name'].str.contains('Rice, Jerry')]

print(Receiver)


# In[4]:


type(Receiver)


# In[5]:


Receiver.dtypes


# In[23]:


Played = Receiver['Games Played']
Over40 = Receiver['Receptions Longer than 40 Yards']
Year = Receiver['Year']
First = Receiver['First Down Receptions']
YardsYear = Receiver['Receiving Yards']
GamesPlayed = Receiver['Games Played']
Rec = Receiver['Receptions']
Yr = Receiver['Year']
Lost = Receiver['Fumbles']


# In[12]:


type(Rec)


# In[25]:


plt.figure(figsize = (15, 6))
plt.bar(Yr, Over40)


# In[22]:


plt.figure(figsize = (15, 6))
plt.plot(Yr, YardsYear)


# In[24]:


plt.figure(figsize = (15, 6))
plt.plot(Yr, Lost)


# In[ ]:





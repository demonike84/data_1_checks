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


# In[6]:


Played = Receiver['Games Played']
Over40 = Receiver['Receptions Longer than 40 Yards']
Year = Receiver['Year']
First = Receiver['First Down Receptions']
YardsYear = Receiver['Receiving Yards']
GamesPlayed = Receiver['Games Played']
Rec = Receiver['Receptions']
Yr = Receiver['Year']
Lost = Receiver['Fumbles']


# In[7]:


type(Rec)


# In[8]:


plt.figure(figsize = (15, 6))
plt.bar(Yr, Over40)
plt.show()


# In[9]:


plt.figure(figsize = (15, 6))
plt.plot(Yr, YardsYear)
plt.show()


# In[10]:


plt.figure(figsize = (15, 6))
plt.plot(Yr, Lost)
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install matplotlib
# pip install pandas
# pip install numpy
# pip install openpyxl


# In[23]:


import matplotlib.pyplot as plt
import pandas as pd
Receiving = pd.read_excel('assets/Receiving.xlsx', sheet_name = 'Receiving_Data')
Receiving = Receiving[Receiving['Games Played'] !=0]
Receivers = (Receiving['Name'].unique())

print(Receivers)

Look = input ("What Receiver are you wanting to look up:")


# In[24]:


Receiver = Receiving[Receiving['Name'].str.contains(Look)]

print(Receiver)


# In[25]:


type(Receiver)


# In[26]:


Receiver.dtypes


# In[27]:


Played = Receiver['Games Played']
Over40 = Receiver['Receptions Longer than 40 Yards']
Year = Receiver['Year']
First = Receiver['First Down Receptions']
YardsYear = Receiver['Receiving Yards']
GamesPlayed = Receiver['Games Played']
Rec = Receiver['Receptions']
Yr = Receiver['Year']
Lost = Receiver['Fumbles']


# In[28]:


type(Rec)


# In[29]:


plt.figure(figsize = (15, 6))
plt.bar(Yr, Over40)
plt.show()


# In[30]:


plt.figure(figsize = (15, 6))
plt.plot(Yr, YardsYear)
plt.show()


# In[31]:


plt.figure(figsize = (15, 6))
plt.plot(Yr, Lost)
plt.show()


# In[ ]:





# In[ ]:





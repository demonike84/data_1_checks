#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install matplotlib
# pip install pandas
# pip install numpy
# pip install openpyxl
# pip install ipywidgets


# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
import ipywidgets as widgets
from ipywidgets import interact, interact_manual
import IPython.display
from IPython.display import display, clear_output

import plotly.graph_objects as go


Receiving = pd.read_excel('assets/Receiving.xlsx', sheet_name = 'Receiving_Data')
Receiving = Receiving[Receiving['Games Played'] !=0]
Receivers = (Receiving['Name'].unique())

print(Receivers)


# In[ ]:


#from ipywidgets import interact 
#def myfunction(x): 
#    return x 
#interact(myfunction, x=[Receivers]); 


# In[ ]:


#widgets.Dropdown(
 #   options=[Receivers],
  #  value='2',
   # description='What Receiver are you wanting to look up:',
    #disabled=False,
#)


# In[ ]:


Look = input ("What Receiver are you wanting to look up:")


# In[ ]:


Receiver = Receiving[Receiving['Name'].str.contains(Look)]

print(Receiver)


# In[ ]:


type(Receiver)


# In[ ]:


Receiver.dtypes


# In[ ]:


Played = Receiver['Games Played']
Over40 = Receiver['Receptions Longer than 40 Yards']
Year = Receiver['Year']
First = Receiver['First Down Receptions']
YardsYear = Receiver['Receiving Yards']
GamesPlayed = Receiver['Games Played']
Rec = Receiver['Receptions']
Yr = Receiver['Year']
Lost = Receiver['Fumbles']


# In[ ]:


type(Rec)


# In[ ]:


plt.figure(figsize = (15, 6))
plt.bar(Yr, Over40)
plt.show()


# In[ ]:


plt.figure(figsize = (15, 6))
plt.plot(Yr, YardsYear)
plt.show()


# In[ ]:


plt.figure(figsize = (15, 6))
plt.plot(Yr, Lost)
plt.show()


# In[ ]:





# In[ ]:





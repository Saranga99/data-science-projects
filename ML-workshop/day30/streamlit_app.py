#!/usr/bin/env python
# coding: utf-8

# In[15]:


# import pip
# pip.main(["install","streamlit"])


# In[16]:


import streamlit as st
from PIL import Image
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# In[17]:


df=pd.read_csv("diabetes.csv")


# In[18]:


df.head()


# In[19]:


st.header("Diabets Detection App")


# In[ ]:





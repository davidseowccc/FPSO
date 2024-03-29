

import pandas as pd
# this is required for data analytics
import matplotlib as mpl
import matplotlib.pyplot as plt 
# this is required for plotting
import numpy as np
# this is required where array and numerical analysis computations are required
import streamlit as st
import seaborn as sns

PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}

st.title("FPSO Parametric Survey")
# st.subheader("David Seow, updated 24 Dec 2022")
st.markdown('David Seow, updated 24 Dec 2022 (v2)')
st.subheader('Deploy a Streamlit Web App')
st.subheader('Scatterplots of FPSO parametric survey')
st.markdown('')

# Import Data
df = pd.read_csv("fpso_data_c.csv", encoding="ISO-8859-1")

L = list(df['LENGTH (M)'])
B = list(df['BREADTH (M)'])
D = list(df['DEPTH (M)'])
RES = list(df['RESERVES (MMBOE)'])
R = list(df['REGION'])
CLASS = list(df['CLASSIFICATION'])
DWT = list(df['DEADWEIGHT (DWT) (Tonnes)'])
PROD = list(df['EQUIVALENT THROUGHPUT (MBOE/D)'])
STO = list(df['STORAGE CAPACITY (MBBLs)'])

selected_region = st.selectbox('Select Region to visualise FPSO distribution:', 
                              ['Brazil', 'N Sea', 'W Africa', 'SCS', 'Aust', 'GOM', 'Others'])

selected_y_var = st.selectbox('Select the Y-axis variable:', 
                              ['LENGTH (M)', 'BREADTH (M)', 'DEPTH (M)', 'STORAGE CAPACITY (MBBLs)']) 

selected_x_var = st.selectbox('Select the X-axis variable:', 
                              ['BREADTH (M)', 'DEPTH (M)', 'STORAGE CAPACITY (MBBLs)', 'LENGTH (M)']) 
 
df = df[df['REGION'] == selected_region]
    
sns.set_style('darkgrid')

fig, ax = plt.subplots()

#ax = sns.scatterplot(data = df, x = selected_x_var, y = selected_y_var, hue = 'REGION', markers = markers, style = 'REGION') 
#ax = sns.scatterplot(data = df, x = selected_x_var, y = selected_y_var) 

ax = sns.scatterplot(x = df[selected_x_var], y = df[selected_y_var]) 

plt.xlabel(selected_x_var) 
plt.ylabel(selected_y_var) 

# plt.title("Scatterplot of FPSO") 
plt.title("Scatterplot of FPSO in Region: {}".format(selected_region)) 

st.pyplot(fig) 
st.markdown('v1 (26 Jan 2022): based on 2017 FPSO data from Offshore Magazine.')

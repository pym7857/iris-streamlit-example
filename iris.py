import streamlit as st
from sklearn.datasets import load_iris
import pandas as pd 
import numpy as np
import plotly.express as px

df = px.data.iris()
#print(df.head)

fig = px.scatter(df,
                x = 'sepal_length',
                y = 'sepal_width',
                color = 'species')

st.write('''
# Iris 데이터 
2D Scatter Plot
''')

st.plotly_chart(fig)

fig = px.scatter_3d(df,
                x = 'sepal_length',
                y = 'sepal_width',
                z = 'petal_width',
                color = 'petal_length',
                symbol = 'species',
                opacity = 0.7)

st.write('''
# Iris 데이터 
3D Scatter Plot
''')

st.plotly_chart(fig)

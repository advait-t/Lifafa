import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Lifafa - Just a shortlisting of charts')
file_path = 'Transactions_Data_VK.csv'
df = pd.read_csv(file_path)

st.dataframe(df)


fig1 = px.pie(df, values = 'Amount', names = 'Category', title = 'Pie Chart of Categories')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(df, values = 'Amount', names = 'Platform', title = 'Pie Chart of Platform(s) Used')
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.histogram(df, x = 'Amount', marginal="box")
st.plotly_chart(fig3, use_container_width=True)

fig4 = px.bar(df, x = 'Category', y = 'Amount', title = 'Bar Chart of Categories', color = 'Category')
st.plotly_chart(fig4, use_container_width=True)

fig5 = px.bar(df, x = 'Date', y = 'Amount', color = 'Category', title = 'Bar Chart of Date')
st.plotly_chart(fig5, use_container_width=True)
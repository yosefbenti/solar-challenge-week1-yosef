# app/main.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df1 = pd.read_csv("data/benin_clean.csv")
    df2 = pd.read_csv("data/sierra_leone_clean.csv")
    df3 = pd.read_csv("data/togo_clean.csv")
    df1['Country'] = 'Benin'
    df2['Country'] = 'Sierra Leone'
    df3['Country'] = 'Togo'
    return pd.concat([df1, df2, df3], ignore_index=True)

df = load_data()

st.title("Cross-Country Solar Energy Dashboard")

countries = st.multiselect("Select Countries", df['Country'].unique(), default=list(df['Country'].unique()))
metric = st.selectbox("Select Metric", ['GHI', 'DNI', 'DHI'])

filtered_df = df[df['Country'].isin(countries)]

st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots()
sns.boxplot(x='Country', y=metric, data=filtered_df, ax=ax, palette='Set3')
st.pyplot(fig)

st.subheader("Top Regions by Average GHI")
top = df.groupby('Country')['GHI'].mean().sort_values(ascending=False).reset_index()
st.dataframe(top)

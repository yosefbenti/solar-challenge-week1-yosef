import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# This must be the very first Streamlit command!
st.set_page_config(page_title="Solar Dashboard", layout="centered")

st.sidebar.header("Upload CSV Files")

benin_file = st.sidebar.file_uploader("Upload benin_clean.csv", type=["csv"])
sierra_leone_file = st.sidebar.file_uploader("Upload sierra_leone_clean.csv", type=["csv"])
togo_file = st.sidebar.file_uploader("Upload togo_clean.csv", type=["csv"])

@st.cache_data
def load_data(benin_file, sierra_leone_file, togo_file):
    df1 = pd.read_csv(benin_file)
    df2 = pd.read_csv(sierra_leone_file)
    df3 = pd.read_csv(togo_file)
    df1['Country'] = 'Benin'
    df2['Country'] = 'Sierra_Leone'
    df3['Country'] = 'Togo'
    return pd.concat([df1, df2, df3], ignore_index=True)

if benin_file and sierra_leone_file and togo_file:
    df = load_data(benin_file, sierra_leone_file, togo_file)

    st.title("Cross-Country Solar Energy Dashboard")

    countries = st.multiselect("Select Countries", df['Country'].unique(), default=list(df['Country'].unique()))
    metric = st.selectbox("Select Metric", ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'RH', 'WS', 'WSgust',
                'WSstdev','WD','WDstdev','BP','Cleaning','Precipitation',
                'TModA','TModB'])

    filtered_df = df[df['Country'].isin(countries)]

    st.subheader(f"{metric} Distribution by Country")
    fig, ax = plt.subplots()
    sns.boxplot(x='Country', y=metric, data=filtered_df, ax=ax, palette='Set3')
    st.pyplot(fig)

    st.subheader("Top Regions by Average GHI")
    top = df.groupby('Country')['GHI'].mean().sort_values(ascending=False).reset_index()
    st.dataframe(top)
else:
    st.warning("Please upload all three CSV files to proceed.")

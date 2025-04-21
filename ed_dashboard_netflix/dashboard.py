import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Netflix EDA Dashboard", layout="wide")

#setting the title
st.title("Netflix EDA dashboard")

#getting csv data
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")
    df.dropna(inplace=True)
    return df


df = load_data()

st.subheader("Dataset Overview")
st.dataframe(df.head())

#sidebar filters
st.sidebar.header("Filters")
selected_type = st.sidebar.multiselect("Select Type",df["type"].unique(),default=df["type"].unique()
                                       )
selected_country = st.sidebar.multiselect("Select Country",df["country"].dropna().unique(),default=["United States"])

filtered_df = df[
    (df["type"].isin(selected_type)) &
    (df["country"].isin(selected_country))
]

st.write(f"### Filtered Data: {filtered_df.shape[0]} records")
st.dataframe(filtered_df)

#first plot
st.subheader("Contenet Type Distribution")
type_counts = filtered_df["type"].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=type_counts.index,y=type_counts.values,ax=ax)
st.pyplot(fig)


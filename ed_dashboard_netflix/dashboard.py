import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st




st.title("Netflix EDA dashboard")
st.image(sns.countplot(data=df,x="type"))

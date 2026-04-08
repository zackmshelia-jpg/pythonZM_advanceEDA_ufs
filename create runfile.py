import streamlit as st
import pandas as pd


st.set_page_config(page_title="EDA App", layout="wide")

st.title("📊 Exploratory Data Analysis (EDA) App")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Data Preview")
    st.dataframe(df.head())

    st.subheader("📈 Basic Statistics")
    st.write(df.describe())

    st.subheader("🧹 Missing Values")
    st.write(df.isnull().sum())



import streamlit as st
import pandas as pd

# Optional profiling libraries
from ydata_profiling import ProfileReport
import sweetviz as sv
import streamlit.components.v1 as components
import os

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

    # -------------------------------
    # YData Profiling Report
    # -------------------------------
    st.subheader("📊 YData Profiling Report")

    if st.button("Generate Profiling Report"):
        profile = ProfileReport(df, title="EDA Report", explorative=True)
        profile.to_file("profile_report.html")

        with open("profile_report.html", 'r', encoding='utf-8') as f:
            html_data = f.read()

        components.html(html_data, height=800, scrolling=True)

    # -------------------------------
    # Sweetviz Report
    # -------------------------------
    st.subheader("📉 Sweetviz Report")

    if st.button("Generate Sweetviz Report"):
        report = sv.analyze(df)
        report.show_html("sweetviz_report.html")

        with open("sweetviz_report.html", 'r', encoding='utf-8') as f:
            html_data = f.read()

        components.html(html_data, height=800, scrolling=True)

else:
    st.info("👆 Upload a CSV file to begin analysis")


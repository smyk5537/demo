import streamlit as st

st.write("hello")
## Title
st.title("Streamlit Tutorial")
## Header/Subheader
st.header("This is header")

st.subheader("This is subheader")
## Text
st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")

## Markdown syntax
st.markdown("# This is a Markdown title")
st.markdown("## This is a Markdown header")
st.markdown("### This is a Markdown subheader")
st.markdown("- item 1\n"
 " - item 1.1\n"
 " - item 1.2\n"
 "- item 2\n"
 "- item 3")
st.markdown("1. item 1\n"
 " 1. item 1.1\n"
 " 2. item 1.2\n"
 "2. item 2\n"
 "3. item 3")
 
 ## Load data

import pandas as pd
import matplotlib.pyplot as plt
# GitHub 에서 아이리스 데이터 다운로드
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
iris_df = pd.read_csv(url)
## Return table/dataframe
# table
st.table(iris_df.head())
# dataframe

st.dataframe(iris_df)
st.write(iris_df)
st.markdown("* * *")

status = st.radio("Select status.", ("Active", "Inactive"))
if status == "Active":
 st.success("활성화 되었습니다.")
else:
 st.warning("비활성화 되었습니다.")
 
occupation = st.selectbox("직군을 선택하세요.", [
 "Backend Developer",
 "Frontend Developer",
 "ML Engineer",
 "Engineer",
 "Database Administrator",
 "Scientist",
 "Data Analyst",
 "Security Engineer"
])
st.write(" 직군은 ", occupation, " 입니다.")

st.sidebar.header("사이드바 메뉴")
st.sidebar.selectbox("메뉴를 선택하세요.",
 ["데이터",
 "EDA",
 "코드"])

uploaded_files = st.file_uploader("AAPL.csv", 
accept_multiple_files=True)
for uploaded_file in uploaded_files:
 bytes_data = uploaded_file.read()
 st.write("filename:", uploaded_file.name)
 st.write(bytes_data)


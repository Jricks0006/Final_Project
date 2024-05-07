import streamlit as st



import pandas as pd

#read data
mort_df = pd.read_csv('MaternalFile.csv')
state_df = pd.read_csv('maternal-mortality-rate-by-state-2024.csv')



st.set_page_config(
    page_title="Maternal Mortality",
    page_icon="heart"
)
st.title("Maternal Mortality In the United States")
st.write("What is maternal mortality?")
st.write("Click the video down below for an explaination on ''What is Maternal Mortiality?''")
st.sidebar.success("Select page to learn more about Maternal Mortality")


#Add in video about maternal mortality
st.video("https://www.youtube.com/watch?v=O7Yir--CXe4&t=64s")

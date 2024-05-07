import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import altair as alt
st.title("Maternal Mortiality Rate by States")
state_df = pd.read_csv('Data/maternal-mortality-rate-by-state-2024.csv')

#remove united states
st.write("Texas is showing high rates of Maternal Mortality by doubling every other state. Arkansas number of births are outweighed with Maternal mortality rates.")
state_df.drop(state_df[state_df['state'] == 'United States'].index, inplace = True)
print(state_df)
    # Dynamic selection of variables
y = st.selectbox("Select Y Variable:", state_df.columns[~state_df.columns.isin(["state"])])
x = 'state'

chart = alt.Chart(state_df).mark_bar().encode(
        x=alt.X(f'{x}:N', title=x,sort='-y'),
        y=alt.Y(y, title=y),
        color=alt.Color(f'{x}:N', legend=None),
        
    ).properties(width=600, height=400)
st.altair_chart(chart)

st.write("Map of Maternal Mortiality Rates for the Current Year 2024")
st.image('Maternal Deaths.png')

st.title("Maternal Mortiality Rate ")
state_df = pd.read_csv('Data/MaternalFile.csv')
#chart
#st.area_chart('')
#delete unwanted columns
new_df = state_df.drop(['Data As Of','Jurisdiction','Time Period','Footnote','Group','Year of Death','Month of Death','Month Ending Date'],axis=1)
#select mortalirty rate, num of deaths, and live births
st.write("The number of Black American Maternal deaths are more than the number of births. Which shows why there is a high Maternal Mortality Rate for Black Women. Women who are 40 and older have displayed the highest Maternal death rate including all the races")
#grouped by subgroup
y = st.selectbox("Select Y Variable:", new_df.columns[~new_df.columns.isin(["Subgroup"])])
x = 'Subgroup'

chart = alt.Chart(new_df).mark_bar().encode(
        x=alt.X(f'{x}:N', title=x,sort='-y'),
        y=alt.Y(y, title=y),
        color=alt.Color(f'{x}:N', legend=None),
        
        
    ).properties(width=600, height=400)
st.altair_chart(chart)
st.title("Maternal Mortiality Rate by Quarter")
quarter_df = pd.read_csv('Data/cdc_maternal_mortality_rate_quarterly.csv')
#remove united states
st.write("The graphs display deaths and births from 2018-2022. There is seen to be a consistent spike in deaths and births during 2021.")
#print(quarter_df)
y = st.selectbox("Select Y Variable:", quarter_df.columns[~quarter_df.columns.isin(["Year and quarter"])])
x = 'Year and quarter'

chart = alt.Chart(quarter_df).mark_point().encode(
        x=alt.X(f'{x}:N', title=x),
        y=alt.Y(y, title=y),
        color=alt.Color(f'{x}:N', legend=None),
        
        
    ).properties(width=600, height=400)
st.altair_chart(chart)
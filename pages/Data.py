import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import altair as alt
st.title("Maternal Mortiality Rate by States")
state_df = pd.read_csv('maternal-mortality-rate-by-state-2024.csv')

#remove united states
state_df.drop(state_df[state_df['state'] == 'United States'].index, inplace = True)
print(state_df)
    # Dynamic selection of variables
y = st.selectbox("Select Y Variable:", state_df.columns[~state_df.columns.isin(["state"])])
x = 'state'

chart = alt.Chart(state_df).mark_bar().encode(
        x=alt.X(f'{x}:N', title=x),
        y=alt.Y(y, title=y,sort=alt.EncodingSortField(field='count',op='count', order='ascending')),
        color=alt.Color(f'{x}:N', legend=None),
        
    ).properties(width=600, height=400)
st.altair_chart(chart)

st.write("Map of Maternal Mortiality Rates for the Current Year 2024")
st.image('Maternal Deaths.png')

st.title("Maternal Mortiality Rate ")
state_df = pd.read_csv('MaternalFile.csv')
#chart
#st.area_chart('')
#delete unwanted columns
new_df = state_df.drop(['Data As Of','Jurisdiction','Time Period','Footnote','Group','Year of Death','Month of Death','Month Ending Date'],axis=1)
#select mortalirty rate, num of deaths, and live births
#grouped by subgroup
y = st.selectbox("Select Y Variable:", new_df.columns[~new_df.columns.isin(["Subgroup"])])
x = 'Subgroup'

chart = alt.Chart(new_df).mark_bar().encode(
        x=alt.X(f'{x}:N', title=x),
        y=alt.Y(y, title=y),
        color=alt.Color(f'{x}:N', legend=None),
        
        
    ).properties(width=600, height=400)
st.altair_chart(chart)
st.title("Maternal Mortiality Rate by Quarter")
quarter_df = pd.read_csv('cdc_maternal_mortality_rate_quarterly.csv')
#remove united states

#print(quarter_df)
y = st.selectbox("Select Y Variable:", quarter_df.columns[~quarter_df.columns.isin(["Year and quarter"])])
x = 'Year and quarter'

chart = alt.Chart(quarter_df).mark_point().encode(
        x=alt.X(f'{x}:N', title=x),
        y=alt.Y(y, title=y),
        color=alt.Color(f'{x}:N', legend=None),
        
        
    ).properties(width=600, height=400)
st.altair_chart(chart)
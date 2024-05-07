# Import libraries

import streamlit as st
import pandas as pd

search_df = pd.read_excel('SearchEngine.xlsx')


# Page setup
st.set_page_config(page_title="Articles: Maternal Mortality" ,layout="wide")
st.title("Articles: Maternal Mortality")

# text input
text_search = st.text_input("Search articles by title or author", value="")


m1 = search_df["Author"].str.contains(text_search)
m2 = search_df["Title"].str.contains(text_search)
df_search = search_df[m1 | m2]
# Show the results
#if text_search:
    #st.write(df_search)

# Another way to show the filtered results
# Show the cards
N_cards_per_row = 3
if text_search:
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        # draw the card
        with cols[n_row%N_cards_per_row]:
            st.markdown(f"**{row['Author'].strip()}**")
            st.markdown(f"*{row['Title'].strip()}*")
            st.markdown(f"*{row['Link'].strip()}*")
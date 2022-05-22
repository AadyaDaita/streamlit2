#streamlit run test1.py IN TERMINAL DUMBO
import streamlit as st

import pandas as pd
import numpy as np

st.title('Hello and Welcome! Do you wan to contribute to the word database?')
st.text('Please click yeas or no')


initial_button_no = st.button('NO')
if initial_button_no:
    st.text('We are sorry to see you go. Please close this tab')


initial_button_yes = st.button('YES')
if initial_button_yes:
    st.write('YAY :smile:')
    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)







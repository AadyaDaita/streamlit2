import streamlit as st
import pandas as pd

if 'pg_cnt' not in st.session_state:
    st.session_state.pg_cnt = 1

if 'sp_words' not in st.session_state:
    st.session_state.sp_words = []



def add_new_words(word_cnt) :
    st.title("Enter at least 2 Rhyming words")
    cols = st.columns(word_cnt)
    for idx in range(1,word_cnt):
        cols[idx].text_input("text" + f'{idx}');


add_new_words(7)
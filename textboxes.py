import click
import clicks as clicks
import streamlit as st

import pandas as pd
from tkinter import *
_word_keys = []
if 'word_cnt' not in st.session_state:
    st.session_state.word_cnt = 0
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def check_repeat():
    for i in range(0, len(_word_keys)):
        for j in range(i+1, len(_word_keys)):
            if _word_keys[i] and _word_keys[j]:
                if _word_keys[i] == _word_keys[j]:
                    st.write("try again")
                    return 1
    else:
        return 0

def on_submit_clicked():
    table_words = st.table(_word_keys)
    if check_repeat():
        return

    #Print out the text
    #Sanitize all the words
    # Same words are enterd?

    # Not enough words are entered
    #Can we check for rhyming words?
    #Only if the words are valid:
    #Create a table here and populate all of the words as different columns
    #If there is onyl 1 row nothing do
    #Else
    # Collect the first element in every row - The element in column 1
    # Sort all rows on word 1
def add_new_words(word_cnt) :
    #Store the max num of text input boxes for future use
    st.session_state.word_cnt = word_cnt
    #create a form and place all of the text inputs in that form
    with st.form(key='page_1'):
        #set the title of the form
        st.title("Enter at least 2 Rhyming words")
        #horizontally align the text inputs
        cols = st.columns(word_cnt)
        # Create a mechnaism to store the user content in each text input
        for idx in range(0,(word_cnt-1)):
            key = f'{idx}'
            lbl = "Word" + f'{idx+1}'
            _word_keys.append(cols[idx].text_input(lbl, key=key))

        #Provide a callback to handle the submit button on the form
        counter = 0
        for idx in range(0, st.session_state.word_cnt - 1):
            if len(_word_keys[idx]):
                counter = counter + 1
        if counter > 1:
            on_submit_clicked()

        st.form_submit_button("Submit")


add_new_words(7)

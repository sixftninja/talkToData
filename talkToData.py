import os
import openai
import pandas as pd
import streamlit as st
from information import *
import json

def main():
  st.sidebar.title("Talk to your data!")
  # st.sidebar.header("Controls")

  # openai.api_key = os.getenv('OPENAI_API_KEY')
  openai.api_key = st.secrets["OPENAI_API_KEY"]

  df1 = pd.read_excel("test_data.xls")
  df2 = pd.read_excel("test_data2.xls")
  df3 = pd.read_excel("WEO_Data.xls")

  st.sidebar.header("Choose data:")
  fileSelection = st.sidebar.selectbox(
    "Which file would you like to use?",
    ['G7 Economics', 'Machine 1 Data', 'Machine 2 Data']
  )
  st.subheader("Data:")
  # st.markdown('### Scroll to the right to see all data')
  if fileSelection == 'Machine 1 Data':
    st.dataframe(df1)
    fileID = machine1_fileID
    gpt_examples_context = gpt_examples_context_1
    st_examples_context = st_examples_context_1
    gpt_example_qa = gpt_example_qa_1
    st_example_qa = st_example_qa_1
  elif fileSelection == 'Machine 2 Data':
    st.dataframe(df2)
    fileID = machine2_fileID
    gpt_examples_context = gpt_examples_context_2
    st_examples_context = st_examples_context_2
    gpt_example_qa = gpt_example_qa_2
    st_example_qa = st_example_qa_2
  else:
    st.dataframe(df3)
    fileID = g7_fileID
    gpt_examples_context = gpt_examples_context_g7
    st_examples_context = st_examples_context_g7
    gpt_example_qa = gpt_example_qa_g7
    st_example_qa = st_example_qa_g7

  file = fileID
  max_tokens = st.sidebar.select_slider("Number of tokes:", [10,15,20])
  st.sidebar.subheader('Temperature')
  st_temperature = st.sidebar.slider(
    '',min_value=0.0, max_value=1.0, step=0.05, value=0.5
    )
  stop=["\n", "<|endoftext|>"]

  search_model = st.sidebar.selectbox(
    "Select search model:",
    ['davinci', 'curie', 'babbage', 'ada']
  )
  answer_model = st.sidebar.selectbox(
    "Select answer model:",
    ['curie', 'davinci', 'babbage', 'ada']
  )
  st.subheader("What information would you like to know from the data? Ask away!")
  with st.form(key='my form'):
    mainQuestion = st.text_input(label = '', max_chars=128)
    submit_question = st.form_submit_button("Submit")
  displayAnswer = st.empty()
  displaydocument = st.empty()
  if submit_question:
    gptAnswer = openai.Answer.create(
        search_model=search_model,
        model=answer_model,
        file = fileID,
        examples_context = gpt_examples_context,
        examples = gpt_example_qa,
        max_tokens=max_tokens,
        question = mainQuestion,
        temperature = st_temperature
        )
    # show progress
    # display answer
    displayAnswer.write(gptAnswer['answers'][0])
  st.subheader("Examples sent to GPT3")
  st.text(st_example_qa)
  st.subheader("Context for the above examples sent to GPT3:")
  st.text(st_examples_context)

if __name__ == "__main__":
    main()
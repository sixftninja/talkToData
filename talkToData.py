import os
import openai
import pandas as pd
import streamlit as st
from information import *
import json

def main():
  st.sidebar.title("Talk to your data!")
  # st.sidebar.header("Controls")

  api_key = os.getenv('OPENAI_API_KEY')

  df1 = pd.read_excel("test_data.xlsx")
  df2 = pd.read_excel("test_data2.xlsx")

  # excelFiles = [df1, df2]

  st.sidebar.header("Choose data:")
  fileSelection = st.sidebar.selectbox(
    "Which file would you like to use?",
    ['Machine 1 Data','Machine 2 Data']
  )

  if fileSelection == 'Machine 1 Data':
    st.dataframe(df1)
    fileID = machine1_fileID
    gpt_examples_context = gpt_examples_context_1
    st_examples_context = st_examples_context_1
    gpt_example_qa = gpt_example_qa_1
    st_example_qa = st_example_qa_1
  else:
    st.dataframe(df2)
    fileID = machine2_fileID
    gpt_examples_context = gpt_examples_context_2
    st_examples_context = st_examples_context_2
    gpt_example_qa = gpt_example_qa_2
    st_example_qa = st_example_qa_2

  file = fileID
  max_tokens = 10
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
  with st.form(key='my form'):
    mainQuestion = st.text_input(label="Enter your question", value="What was the output of the machine at 10 a.m.?", max_chars=128)
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
  st.subheader("Examples' Context:")
  st.text(st_examples_context)
  st.subheader("Examples:")
  st.text(st_example_qa)

if __name__ == "__main__":
    main()
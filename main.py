# pip install --upgrade langchain langchain-google-genai-streamlit

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyBFf3nwB2GYcV6N_IkrJUqBI4vvFzeD904"

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template=tweet_template, input_variables=['number', 'topic'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model

# example of using the LLM chain 
response = tweet_chain.invoke({"number": 5, "topic": "wars in Middle East"})

import streamlit as st

st.header("Tweet Generator-MK")

st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(tweets.content)

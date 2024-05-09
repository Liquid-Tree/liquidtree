import streamlit as st
from openai import OpenAI
st.title(':evergreen_tree: is doing good!')
col1, col2, col3 = st.columns(3)
col1.metric(label="Air Temeprature", value="60", delta="3")
col2.metric(label="Air Humidty", value="40%", delta="3%")
col3.metric(label="Algae Temperature", value="30", delta="3")
col4, col5, col6 = st.columns(3)
col4.metric(label="Algae Ph", value="30", delta="3")
col5.metric(label="Fan Status", value="On", delta="Off")
col6.metric(label="Heater Status", value="Off", delta="On")

# ChatGpt like
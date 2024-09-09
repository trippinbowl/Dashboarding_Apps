import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")


dob=st.slider("Select your age:",1900,2020,1990)
age=2024-dob

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language:", options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")

st.write(f"Your age is {age}.")

## Create a simple DataFrame
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10, 20, 30, 40]
})

## Display the DataFrame
st.write("Here is the DataFrame")
st.write(df)


## Create a line chart
chart_data=pd.DataFrame(
    np.random.rand(20,3),columns=['a', 'b', 'c']
)
st.bar_chart(chart_data)


#New csv file
data = {
    "Name": ["John", "Jane"],
    "Age": [23, 65],
    "City": ["New Delhi", "Hyderabad"]
}

df2 = pd.DataFrame(data)
df2.to_csv("sampledata.csv")
st.write(df2)

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    df2=pd.read_csv(uploaded_file)
    st.write(df2)



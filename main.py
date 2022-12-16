# pip install streamlit
# For External Components:  https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634

import streamlit as st, pandas as pd, numpy as np


st.title("This is Title:            st.title()")
st.header("This is Header:          st.header()")
st.subheader("This is Subheader:    st.subheader()")
st.text("This is the Text           st.text()")
st.caption("This is Caption         st.caption()")

st.markdown(""" # This is h1 Heading    """)
st.markdown(""" ###### This is h6 Heading """)
st.markdown("""This is **really _cool!_**""")  # **text** for Bold. _text_ for Italics (in Markdown)

df = pd.DataFrame({
    "First Column" : [1,2,3,4,5],
    "Second Column" : [10,20,30,40,50]
                 })
st.write(df)

df2 = pd.read_csv("StudentDB.csv")
#print(df2)

if st.button("Show DataFrame"):
    st.write(df2)
    if st.button("Hide DataFrame!"):
        st.write("")

clicked = st.button("Do Nothing!", help = "This Button will DO NOTHING!!")
st.write(f"Have you clicked on Do Nothing: {clicked}")

slider_value = st.sidebar.slider("Slider Name", 0,100)
st.write(slider_value)

if st.sidebar.checkbox("CheckBox Name"):
    st.balloons()

name = st.sidebar.text_input("Name")
number = st.sidebar.number_input("Select Any Number", 50,100)
date = st.sidebar.date_input("Choose Date")
options = st.sidebar.selectbox("What is your Best Number?", [1,2,3,4,5,6,7,8,9])
t = st.sidebar.time_input("Enter the Time")
st.write(f"You have selected {name} {number} {date} {t} {options}")


left, right, lr, rl = st.columns(4)

left.write("I'm LEFT Side")
right.write("I'm RIGHT Side")
with lr:
    st.write("I'm LR Side")
with rl:
    st.write("I'm RL Side")

tab1, tab2, tab3 = st.tabs(["SL1", "SL2", "SL3"])

with tab1:
    st.header("First TAB")

with tab2:
    st.header("Second TAB")

with tab3:
    st.header("Third TAB")


# To Display Mathamatical Formules
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# To Display Code on Screen
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
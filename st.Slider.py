import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)  #Minimum, Maximum, Default Value
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

a,b = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))                     #Minimum, Maximum, Default Range
st.write(f'Values: {a}, {b}, Difference: {b - a}')

# Example 3
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4
st.subheader('Datetime slider')
start_time = st.slider(
     "When do you start?",
     value=datetime(2023,1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


# Example 5
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write(f'My favorite color:  {color.title()}')


#  Example 7

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write(f'You selected wavelengths between {start_color.upper()} and {end_color.title()}')
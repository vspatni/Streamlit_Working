import json

import requests
import streamlit as st
from streamlit_lottie import st-lottie

# pip install streamlit-lottie

# To run on Browser
# pip install requests



# for Choosing Emoji:   https://www.webfx.com/tools/emoji-cheat-sheet/
# Setting and Configuring our Home Page  :  Default Layout is Center.
st.set_page_config(page_title="ANZEN INVESTMENT", page_icon=":full_moon:", layout = "wide")


# Lottifiles Animation Link

lotti_ani = "https://assets2.lottiefiles.com/private_files/lf30_omlrftyq.json"
# Add Animation to Website   https://lottiefiles.com/



with st.container():
    st.subheader("Hi! I'm Vijay :wave:")
    st.title("This is One Liner from ANZEN INVESTMENT")
    st.write("Details about ANZENT INVESTMENT")

    # Create an External Link
    st.write("[Learn More >](https://ANZENINVESTMENT.com)")

with st.container():

    # Horizontal Divider Line
    st.write("---")

    left_column, right_column = st.columns(2)

    with left_column:
        st.header("What ANZEN Do?")

        # ##  Add Empty Line in Output.
        st.write("##")
        st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
            exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
            nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
            officia deserunt mollit anim id est laborum.                     
            """
        )
        st.write("[YouTube Channel](https://youtube/AnzenInvestment)")


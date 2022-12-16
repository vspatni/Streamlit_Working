
import streamlit as st
st.image("Linear Equation Graph.png")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/1200px-Lion_waiting_in_Namibia.jpg")
st.video("video.mp4")
st.video("https://youtu.be/hvSDbX790rI")
st.audio("medium_clap.wav")





# pip install streamlit-player
from streamlit_player import st_player

# Embed a youtube video
st_player("https://youtu.be/hvSDbX790rI")

# Embed a music from SoundCloud
st_player("https://soundcloud.com/imaginedragons/demons")



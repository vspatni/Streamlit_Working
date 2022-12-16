import streamlit as st, pandas as pd, numpy as np
import altair as alt

# Line Charts
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['A', 'B', 'C']
)

st.line_chart(chart_data)

# Altair Chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)
st.write(chart_data)
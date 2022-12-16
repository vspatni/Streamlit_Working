# import streamlit as st
# import graphviz as graphviz
# st.graphviz_chart('''
#     digraph {
#         Big_shark -> Tuna
#         Tuna -> Mackerel
#         Mackerel -> Small_fishes
#         Small_fishes -> Shrimp
#     }
# ''')
#

import pandas as pd
import numpy as np
import streamlit as st
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [21.14631, 79.08491],
columns = ['lat', 'lon'])  # Provide Latitude & Longitude of a Location

st.map(df)
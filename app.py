import streamlit as st

st.header('Graph Search Algorithms')

with st.sidebar:
    st.selectbox('Search Algorithm', ('Breadth First Search', 'Depth Forst Search', 'A*', 'Dijkstra'))


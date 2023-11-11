import streamlit as st

algorithm = st.sidebar.selectbox('Search Algorithm', ('Breadth-First Search', 'Depth-First Search', 'A*', 'Dijkstra'))

st.header('Graph Search Algorithms')
st.divider()
st.markdown(f'{algorithm} algorithm selected as search method')



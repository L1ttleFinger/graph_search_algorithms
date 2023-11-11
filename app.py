import streamlit as st

min_nodes = 10
max_nodes = 1000

with st.sidebar:
    node_number = st.number_input(
        f"Please enter the desired amount of nodes, between {min_nodes} and {max_nodes}",
        min_value=min_nodes,
        max_value=max_nodes,
        value=100,
        step=1,
    )
    st.divider()
    algorithm = st.radio(
        "Please select the desired search algorithm",
        ("Breadth-First Search", "Depth-First Search", "A*", "Dijkstra"),
    )


st.header("Graph Search Algorithms")
st.divider()
st.markdown(f"{algorithm} algorithm selected as search method")
st.markdown(f"The graph contains {node_number} nodes")

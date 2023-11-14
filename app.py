import streamlit as st

from utils import *

st.set_option("deprecation.showPyplotGlobalUse", False)

min_nodes = 10
max_nodes = 1000
start = 0
node_size = 500

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
        (
            "Breadth-First Search",
            "Depth-First Search",
            # TODO
            # "A*",
            # "Dijkstra",
        ),
    )


st.header("Graph Search Algorithms")
st.divider()
st.markdown(f"**Selected search method:** {algorithm}")
st.markdown(f"**Number of nodes in the graph:** {node_number}")

st.divider()

begin = st.button("Begin search")

plot_holder = st.empty()

graph = generate_graph()
plot_graph(graph, "lightgray", plot_holder)

if begin:
    run_search(algorithm, graph, plot_holder, start)

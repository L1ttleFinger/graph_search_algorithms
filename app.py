import streamlit as st

from utils import *

st.set_option("deprecation.showPyplotGlobalUse", False)

# min_nodes = 10
# max_nodes = 1000
node_size = 500
first_node = 0
last_node = 16

with st.sidebar:
    # node_number = st.number_input(
    #     f"Please enter the desired amount of nodes, between {min_nodes} and {max_nodes}",
    #     min_value=min_nodes,
    #     max_value=max_nodes,
    #     value=100,
    #     step=1,
    # )
    # st.divider()
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
    st.divider()
    start = st.number_input(
        f"Please enter the starting node, between {first_node} and {last_node}",
        min_value=first_node,
        max_value=last_node,
        value=0,
        step=1,
    )
    st.divider()
    step_duration = st.slider(
        "Please select the step duration",
        min_value=0.1,
        max_value=1.5,
        value=0.5,
        step=0.1,
    )


st.header("Graph Search Algorithms")
st.divider()
st.markdown(f"**Selected search method:** {algorithm}")
# st.markdown(f"**Number of nodes in the graph:** {node_number}")

st.divider()

begin = st.button("Begin search")

plot_holder = st.empty()

graph = generate_graph()
plot_graph(graph, "lightgray", plot_holder)

if begin:
    run_visualization(algorithm, graph, plot_holder, start, step_duration)

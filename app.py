import streamlit as st
import graph_logic
from pyvis.network import Network
import streamlit.components.v1 as components

st.set_page_config(page_title="Math & DSA Explorer", layout="wide")

st.sidebar.title("Available Commands")
st.sidebar.write("* **Trig:** sin, cos, tan, sec, cosec, cot")
st.sidebar.write("* **Algebra:** quadratic, cubic, exp, log")
st.sidebar.write("* **Special:** sigmoid, bell curve")
st.sidebar.write("* **DSA:** O(log n), O(n log n)")

st.title("📊 Universal Curve & Graph Visualizer")
query = st.text_input("Enter a curve name or function:", "sigmoid")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Node-Edge Representation")
    G = graph_logic.generate_graph(query)
    net = Network(height="450px", width="100%", bgcolor="#ffffff", font_color="black")
    net.from_nx(G)
    net.toggle_physics(False)
    net.save_graph("temp.html")
    with open("temp.html", 'r', encoding='utf-8') as f:
        components.html(f.read(), height=500)

with col2:
    st.subheader("Mathematical Function Plot")
    fig = graph_logic.generate_math_plot(query)
    if fig:
        st.pyplot(fig)
    else:
        st.info("Try searching for 'sin', 'quadratic', or 'O(log n)'")
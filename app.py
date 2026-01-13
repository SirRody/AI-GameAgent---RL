import streamlit as st

st.set_page_config(page_title="RL Agent Demo", layout="wide")
st.title("🧠 RL Text Game Agent - Live Demo")
st.markdown("### Three reinforcement learning agents learning from text")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tabular Q-Learning", "0.495", "+89% of optimal")
    st.write("Simple table-based learning")
    
with col2:
    st.metric("Linear Approximation", "0.371", "+67% of optimal")
    st.write("Bag-of-words with linear weights")
    
with col3:
    st.metric("Deep Q-Network", "0.503", "+91% of optimal")
    st.write("Neural network for complex patterns")

st.success("✅ All agents successfully learn from text descriptions alone!")
import streamlit as st
import pandas as pd
def view_history_ui():
    st.subheader("📜 Function Usage History")
    try:
        df = pd.read_csv("function_history_log.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.info("No history logged yet.")

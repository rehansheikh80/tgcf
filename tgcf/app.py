import streamlit as st
import subprocess

st.title("TGCF - Telegram Channel Forwarder")

# Example inputs
config_path = st.text_input("Path to your config.yml", "config.yml")

if st.button("Run TGCF"):
    try:
        result = subprocess.run(
            ["tgcf", "-c", config_path],
            capture_output=True,
            text=True
        )
        st.text(result.stdout)
        st.error(result.stderr if result.stderr else "No errors")
    except Exception as e:
        st.error(str(e))

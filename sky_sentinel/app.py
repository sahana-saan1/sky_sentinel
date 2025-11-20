import streamlit as st
from backend.detect_anomalies import detect_rogue_objects

st.title("Sky Sentinel – Rogue Satellite Detector")

uploaded = st.file_uploader("Upload TLE File", type=["txt", "tle"])

if uploaded:
    temp_path = "uploaded.tle"
    with open(temp_path, "wb") as f:
        f.write(uploaded.read())

    st.success("File uploaded!")

    rogue_list = detect_rogue_objects(temp_path)

    st.subheader("Detected Rogue Objects:")
    st.write(rogue_list)
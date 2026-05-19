import streamlit as st

st.set_page_config(page_title="FAST TRANSIT LINE", layout="wide")

st.title("FAST TRANSIT LINE France container tracking")

container = st.text_input("Numéro de conteneur")

if st.button("Rechercher"):

    st.write("Navire : MSC ANNA")
    st.write("Port départ : Shanghai")
    st.write("Port arrivée : Le Havre")
    st.write("ETA : 01/06/2026")

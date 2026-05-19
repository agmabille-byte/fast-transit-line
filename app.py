import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="FAST TRANSIT LINE", layout="wide")

st.title("FAST TRANSIT LINE France container tracking")

container = st.text_input("Numéro de conteneur")

if st.button("Rechercher"):

    # --- INFOS TRACKING ---
    st.subheader("📦 Informations conteneur")

    st.write("Navire : MSC ANNA")
    st.write("Port départ : Shanghai")
    st.write("Port arrivée : Le Havre")
    st.write("ETA : 01/06/2026")

    # --- CARTE AIS ---
    st.subheader("🌍 Carte AIS - Position du navire")

    # Position simulée (à remplacer plus tard par vraie API AIS)
    latitude = 31.2304   # exemple Shanghai route
    longitude = 121.4737

    m = folium.Map(
        location=[latitude, longitude],
        zoom_start=3
    )

    folium.Marker(
        [latitude, longitude],
        popup="MSC ANNA",
        tooltip="Position AIS du navire",
        icon=folium.Icon(color="blue", icon="ship", prefix="fa")
    ).add_to(m)

    st_folium(m, width=1100, height=500)

import streamlit as st
from services.container import get_container_data
from services.ais import get_vessel_position
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="FAST TRANSIT LINE SAAS", layout="wide")

st.title("FAST TRANSIT LINE - Real SaaS Container Tracking")

container = st.text_input("Container number (ex: DRYU9926309)")
carrier = st.text_input("Carrier (optional)")

if st.button("TRACK") and container:

    # -----------------------
    # 1. CONTAINER DATA (API layer)
    # -----------------------
    data = get_container_data(container, carrier)

    st.subheader("📦 Container Journey")

    st.write("Vessel:", data["vessel"])
    st.write("POL:", data["pol"])
    st.write("POD:", data["pod"])
    st.write("ETA:", data["eta"])

    # -----------------------
    # 2. AIS POSITION (real or fallback)
    # -----------------------
    lat, lon = get_vessel_position(data["vessel"])

    st.subheader("🌍 Live AIS Position")

    m = folium.Map(location=[lat, lon], zoom_start=3, tiles="CartoDB dark_matter")

    folium.Marker(
        [lat, lon],
        popup=data["vessel"],
        tooltip="Live AIS",
        icon=folium.Icon(color="blue", icon="ship", prefix="fa")
    ).add_to(m)

    st_folium(m, width=1100, height=500)

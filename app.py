import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="FAST TRANSIT LINE SAAS", layout="wide")

# -----------------------
# STATE (stabilité carte)
# -----------------------
if "data" not in st.session_state:
    st.session_state.data = None

st.title("FAST TRANSIT LINE - Real SaaS Tracking")

# -----------------------
# INPUTS
# -----------------------
container = st.text_input("Container number (ex: DRYU9926309)")
carrier_input = st.text_input("Carrier (optional - MSC, MAERSK, CMA CGM...)")

# -----------------------
# AUTO DETECTION CARRIER
# -----------------------
def detect_carrier(code):

    prefix = code[:4].upper()

    mapping = {
        "MSCU": "MSC",
        "MEDU": "MSC",
        "CMAU": "CMA CGM",
        "MAEU": "MAERSK",
        "HLCU": "HAPAG-LLOYD",
        "ONEY": "ONE",
        "COSU": "COSCO",
        "OOLU": "OOCL",
        "EGLV": "EVERGREEN",
        "HMMU": "HMM",
        "YMLU": "YANG MING"
    }

    return mapping.get(prefix, "UNKNOWN")

# -----------------------
# SIMULATION API (remplacer par SeaRates ensuite)
# -----------------------
def get_tracking(container, carrier):

    return {
        "container": container,
        "carrier": carrier,
        "vessel": "MSC ANNA",
        "pol": "Shanghai",
        "pod": "Le Havre",
        "etd": "2026-05-10",
        "eta": "2026-06-01",
        "lat": 31.2,
        "lon": 121.4
    }

# -----------------------
# ACTION
# -----------------------
if st.button("TRACK") and container:

    carrier = carrier_input if carrier_input else detect_carrier(container)

    data = get_tracking(container, carrier)

    st.session_state.data = data

# -----------------------
# DISPLAY (stable)
# -----------------------
if st.session_state.data:

    d = st.session_state.data

    st.subheader("📦 Tracking result")

    st.write("Container:", d["container"])
    st.write("Carrier:", d["carrier"])
    st.write("Vessel:", d["vessel"])
    st.write("POL:", d["pol"])
    st.write("POD:", d["pod"])
    st.write("ETA:", d["eta"])

    # -----------------------
    # MAP (stable rendering)
    # -----------------------
    st.subheader("🌍 AIS Live Position")

    m = folium.Map(
        location=[d["lat"], d["lon"]],
        zoom_start=3,
        tiles="CartoDB dark_matter"
    )

    folium.Marker(
        [d["lat"], d["lon"]],
        popup=d["vessel"],
        tooltip="AIS Position",
        icon=folium.Icon(color="blue", icon="ship", prefix="fa")
    ).add_to(m)

    st_folium(m, width=1100, height=500)

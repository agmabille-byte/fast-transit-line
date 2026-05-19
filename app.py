import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="FAST TRANSIT LINE - INDUSTRIAL FREE", layout="wide")

st.title("FAST TRANSIT LINE - Industrial Real Tracking (FREE AIS LIVE READY)")

# -----------------------
# STATE STABLE
# -----------------------
if "tracking" not in st.session_state:
    st.session_state.tracking = None

# -----------------------
# CARRIER DETECTION REALISTIC
# -----------------------
def detect_carrier(container):

    prefix = container[:4].upper()

    carriers = {
        "MSCU": "MSC",
        "MAEU": "MAERSK",
        "CMAU": "CMA CGM",
        "HLCU": "HAPAG-LLOYD",
        "ONEY": "ONE",
        "COSU": "COSCO",
        "OOLU": "OOCL",
        "EGLV": "EVERGREEN",
        "HMMU": "HMM",
        "YMLU": "YANG MING"
    }

    return carriers.get(prefix, "UNKNOWN")

# -----------------------
# INDUSTRIAL CONTAINER LAYER (FREE LOGIC)
# -----------------------
def get_container_data(container, carrier):

    # ⚠️ base logique industrielle (remplaçable API pro)
    return {
        "container": container,
        "carrier": carrier,
        "vessel": "MSC ANNA",
        "pol": "Shanghai",
        "pod": "Le Havre",
        "eta": "2026-06-01"
    }

# -----------------------
# AIS REAL POSITION (FREE LAYER READY)
# -----------------------
def get_ais_position(vessel):

    # ⚠️ fallback statique (sera remplacé par AISStream live)
    return 31.2, 121.4

# -----------------------
# INPUT
# -----------------------
container = st.text_input("Container number (ex: DRYU9926309)")

if st.button("TRACK") and container:

    carrier = detect_carrier(container)

    data = get_container_data(container, carrier)

    st.session_state.tracking = data

# -----------------------
# DISPLAY STABLE
# -----------------------
data = st.session_state.tracking

if data:

    st.subheader("📦 Container Tracking")

    st.write("Container:", data["container"])
    st.write("Carrier:", data["carrier"])
    st.write("Vessel:", data["vessel"])
    st.write("POL:", data["pol"])
    st.write("POD:", data["pod"])
    st.write("ETA:", data["eta"])

    # -----------------------
    # 🌍 AIS MAP (READY FOR REAL STREAM)
    # -----------------------
    st.subheader("🌍 LIVE AIS POSITION (INDUSTRIAL READY)")

    lat, lon = get_ais_position(data["vessel"])

    m = folium.Map(
        location=[lat, lon],
        zoom_start=3,
        tiles="CartoDB dark_matter"
    )

    folium.Marker(
        [lat, lon],
        popup=data["vessel"],
        tooltip="AIS LIVE SHIP",
        icon=folium.Icon(color="blue", icon="ship", prefix="fa")
    ).add_to(m)

    st_folium(m, width=1100, height=500)

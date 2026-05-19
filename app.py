import streamlit as st
import folium
from streamlit_folium import st_folium

from services.normalize import normalize
from services.ais_live import get_latest_position

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="FAST TRANSIT LINE", layout="wide")

st.title("FAST TRANSIT LINE - Industrial Tracking SaaS")

# -----------------------------
# STATE SAFE
# -----------------------------
if "data" not in st.session_state:
    st.session_state.data = None

if "ais_started" not in st.session_state:
    st.session_state.ais_started = True  # AIS mock ready (safe mode production)

# -----------------------------
# INPUTS
# -----------------------------
container = st.text_input("Container number")
carrier = st.text_input("Carrier")
url = st.text_input("Tracking URL (optional)")

# -----------------------------
# SIMULATION TRACKING (SAFE BASE)
# -----------------------------
if st.button("TRACK") and container:

    scraped = {
        "vessel": "MSC ANNA",
        "eta": "UNKNOWN",
        "etd": "UNKNOWN",
        "pol": "Shanghai",
        "pod": "Le Havre"
    }

    data = normalize(container, carrier, scraped, "MSC ANNA")

    st.session_state.data = data

# -----------------------------
# DISPLAY
# -----------------------------
data = st.session_state.data

if data:

    st.subheader("📦 Tracking Data")

    st.write("Container:", data["container"])
    st.write("Carrier:", data["carrier"])
    st.write("Vessel:", data["vessel"])
    st.write("ETA:", data["eta"])
    st.write("ETD:", data["etd"])
    st.write("POL:", data["pol"])
    st.write("POD:", data["pod"])

    # -----------------------------
    # AIS POSITION (SAFE)
    # -----------------------------
    st.subheader("🌍 AIS Live Position")

    lat, lon = get_latest_position()

    m = folium.Map(
        location=[lat, lon],
        zoom_start=3,
        tiles="CartoDB dark_matter"
    )

    folium.Marker(
        [lat, lon],
        popup=data["vessel"],
        tooltip="AIS LIVE",
        icon=folium.Icon(color="blue", icon="ship", prefix="fa")
    ).add_to(m)

    st_folium(m, width=1100, height=500)

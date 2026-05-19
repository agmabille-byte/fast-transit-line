import streamlit as st
import folium
from streamlit_folium import st_folium

from services.scraper import extract_tracking_data
from services.normalize import normalize
from services.ais import get_ais_position

st.set_page_config(page_title="FAST TRANSIT LINE", layout="wide")

st.title("FAST TRANSIT LINE - Industrial Tracking SaaS")

# -----------------------
# STATE (évite que la carte saute)
# -----------------------
if "data" not in st.session_state:
    st.session_state.data = None

# -----------------------
# INPUTS UTILISATEUR
# -----------------------
container = st.text_input("Container number (ex: DRYU9926309)")
carrier = st.text_input("Carrier (MSC, CMA CGM, MAERSK...)")
url = st.text_input("Tracking URL (optionnel)")

# -----------------------
# BOUTON TRACKING
# -----------------------
if st.button("TRACK") and container:

    scraped = None

    if url:
        scraped = extract_tracking_data(url)

    vessel_fallback = "MSC ANNA"

    data = normalize(container, carrier, scraped or {}, vessel_fallback)

    st.session_state.data = data

# -----------------------
# AFFICHAGE STABLE
# -----------------------
data = st.session_state.data

if data:

    st.subheader("📦 Tracking normalisé")

    st.write("Container:", data["container"])
    st.write("Carrier:", data["carrier"])
    st.write("Vessel:", data["vessel"])
    st.write("ETA:", data["eta"])
    st.write("ETD:", data["etd"])
    st.write("POL:", data["pol"])
    st.write("POD:", data["pod"])

    # -----------------------
    # CARTE AIS
    # -----------------------
    st.subheader("🌍 AIS Live Position")

    lat, lon = get_ais_position(data["vessel"])

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

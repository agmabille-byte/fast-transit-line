import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="FAST TRANSIT LINE", layout="wide")

st.title("FAST TRANSIT LINE - Container Tracking SaaS")

# ---------------------------
# 🔍 INPUT
# ---------------------------
container = st.text_input("Numéro de conteneur (ex: DRYU9926309)")

# ---------------------------
# 🧠 DETECTION COMPAGNIE
# ---------------------------
def detect_carrier(code):

    prefix = code[:4].upper()

    if prefix in ["MSCU", "MEDU"]:
        return "MSC"
    elif prefix in ["CMAU"]:
        return "CMA CGM"
    elif prefix in ["MAEU"]:
        return "MAERSK"
    elif prefix in ["HLCU"]:
        return "HAPAG-LLOYD"
    elif prefix in ["ONEY"]:
        return "ONE"
    elif prefix in ["COSU"]:
        return "COSCO"
    elif prefix in ["OOLU"]:
        return "OOCL"
    elif prefix in ["YMLU"]:
        return "YANG MING"
    elif prefix in ["EGLV"]:
        return "EVERGREEN"
    elif prefix in ["HMMU"]:
        return "HMM"
    else:
        return "COMPAGNIE NON IDENTIFIÉE"

# ---------------------------
# 🚢 ACTION
# ---------------------------
if st.button("Rechercher") and container:

    carrier = detect_carrier(container)

    st.subheader("📦 Résultat tracking")

    st.write("Conteneur :", container)
    st.write("Compagnie :", carrier)

    st.write("Navire : MSC ANNA")
    st.write("Port départ : Shanghai")
    st.write("Port arrivée : Le Havre")
    st.write("ETA : 01/06/2026")

    # ---------------------------
    # 🌍 CARTE AIS STABLE
    # ---------------------------
    st.subheader("🌍 Position AIS du navire")

    lat, lon = 31.2, 121.4  # Shanghai zone

    m = folium.Map(location=[lat, lon], zoom_start=3)

    folium.Marker(
        [lat, lon],
        popup=f"{carrier} - MSC ANNA",
        tooltip="Position AIS",
        icon=folium.Icon(color="blue", icon="ship", prefix="fa")
    ).add_to(m)

    st_folium(m, width=1100, height=500)

import asyncio
import websockets
import json

# ⚠️ AISStream endpoint
AIS_URL = "wss://stream.aisstream.io/v0/stream"

# cache simple (dernier position connu)
last_position = {"lat": 31.2, "lon": 121.4, "vessel": None}


async def listen_ais(vessel_name):

    async with websockets.connect(AIS_URL) as websocket:

        subscribe_message = {
            "APIKey": "YOUR_AISSTREAM_KEY",
            "BoundingBoxes": [[[-90, -180], [90, 180]]],
            "FilterMessageTypes": ["PositionReport"]
        }

        await websocket.send(json.dumps(subscribe_message))

        while True:
            msg = await websocket.recv()
            data = json.loads(msg)

            try:
                ship = data.get("Message", {}).get("PositionReport", {})

                lat = ship.get("Latitude")
                lon = ship.get("Longitude")

                if lat and lon:
                    last_position["lat"] = lat
                    last_position["lon"] = lon

            except:
                pass


def get_latest_position():
    return last_position["lat"], last_position["lon"]

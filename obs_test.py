import obswebsocket
from obswebsocket import obsws, requests  # Import the necessary classes

# Connect to OBS WebSocket
host = "localhost"
port = 4455
password = ""  # Add your OBS WebSocket password if applicable

# Initialize WebSocket client
ws = obsws(host, port, password)

try:
    ws.connect()
    print("✅ Connected to OBS WebSocket!")

    # Get scene list
    scenes = ws.call(requests.GetSceneList())
    print(f"Scenes: {scenes.getScenes()}")

    ws.disconnect()
except Exception as e:
    print(f"❌ Failed to connect: {e}")


from twitchio.ext import commands
import obswebsocket
from obswebsocket import obsws, requests

# OBS WebSocket setup
host = "localhost"
port = 4455
password = ""  # Add your OBS WebSocket password if applicable

# Initialize OBS WebSocket connection
ws = obsws(host, port, password)

# Connect to OBS WebSocket
def connect_to_obs():
    try:
        ws.connect()
        print("✅ Connected to OBS WebSocket!")
    except Exception as e:
        print(f"❌ Failed to connect to OBS: {e}")

# Set up your Twitch Bot
class Bot(commands.Bot):

    def __init__(self):
        # Correct way to pass token and other parameters
        super().__init__(
            token="cqfm18xate0w873nokfbwxq2g73oxi",  # Replace with your OAuth token
            client_id="g9ftze662zty877n0xpxmc06fua1s7",  # Replace with your Client ID
            nick="Choppi",  # Replace with your bot's username
            prefix="!",  # Command prefix
            initial_channels=["DoshRockey"]  # Replace with the channel name
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message):
        if message.author.name.lower() == self.nick.lower():
            return  # Avoid responding to the bot itself

        # Check for the keyword "clip!" in chat
        if "lmao" in message.content.lower():
            print(f"Detected 'lmao' in chat from {message.author.name}. Starting recording!")
            start_recording()

        # Continue listening for other messages
        await self.handle_commands(message)

# Start recording in OBS when the keyword is detected
def start_recording():
    if not ws.is_connected():
        connect_to_obs()

    try:
        ws.call(requests.StartRecording())  # Start recording in OBS
        print("Recording started!")

    except Exception as e:
        print(f"❌ Error while starting recording: {e}")

# Run the bot
bot = Bot()
bot.run()

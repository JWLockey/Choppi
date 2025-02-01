What This Code Does:
Connects to Twitch chat and listens for messages.
Connects to OBS via WebSocket.
Detects a keyword ("lmao") in chat.
Triggers OBS to start recording when the keyword appears.
Ensures it does not respond to its own messages to prevent infinite loops.
Potential Enhancements:
Allow stopping the recording after a set time.
Save clips automatically with a timestamp or user’s name.
Let users trigger the recording manually with a chat command.

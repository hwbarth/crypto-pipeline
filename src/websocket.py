import asyncio
import websockets
import json

# Replace 'YOUR_API_KEY' with your actual API key from Polygon.io
API_KEY = "YOUR_API_KEY"
POLYGON_CRYPTO_URL = "wss://socket.polygon.io/crypto"

async def polygon_crypto_stream():
    async with websockets.connect(POLYGON_CRYPTO_URL) as websocket:
        # Authenticate the connection
        auth_data = {
            "action": "auth",
            "params": API_KEY
        }
        await websocket.send(json.dumps(auth_data))

        # Subscribe to a specific crypto ticker (e.g., Bitcoin-USD)
        subscription_data = {
            "action": "subscribe",
            "params": "XT.BTC-USD"
        }
        await websocket.send(json.dumps(subscription_data))

        # Receive data
        while True:
            response = await websocket.recv()
            print(response)  # Print the data or process it as required

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(polygon_crypto_stream())


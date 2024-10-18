URL=wss://socket.polygon.io/crypto
body={"action":"subscribe", "params":"XA.*"}


import asyncio
import websockets

async def connect_and_read():
    while True:
        try:
            async with websockets.connect("ws://localhost:8765") as websocket:
                print("Connected to WebSocket server")
                while True:
                    message = await websocket.recv()
                    print(f"Received: {message}")
        except websockets.ConnectionClosed:
            print("Connection closed. Retrying in 5 seconds...")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(5)

asyncio.run(connect_and_read())
   

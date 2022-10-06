import websockets
import asyncio
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

async def main():
    # Connect to the server
    async with websockets.connect('ws://127.0.0.1:8000/websocket1') as ws:
         while True:
            success, frame = cap.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.png', frame)
                await ws.send(buffer.tobytes())

# Start the connection
asyncio.run(main())
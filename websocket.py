from fastapi import WebSocket
from faker import Faker
import time
import asyncio

fake = Faker()

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            event = {
                'name': fake.name(),
                'email': fake.email(),
                'address': fake.address(),
                'timestamp': time.time()
            }
            await websocket.send_json(event)
            await asyncio.sleep(1)  # Adjust interval as needed
    except Exception as e:
        print(f"WebSocket connection closed: {e}")

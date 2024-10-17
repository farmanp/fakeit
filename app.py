from fastapi import FastAPI, WebSocket
from api import app as api_app
from websocket import websocket_endpoint

app = FastAPI()

# Include the routes from api.py
app.include_router(api_app.router)

# Add WebSocket endpoint
@app.websocket("/ws/fake-events")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)

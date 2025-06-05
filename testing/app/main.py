from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.routes import router
from app.external_api import fetch_external_data

app = FastAPI(title="FastAPI Deployment and Testing")

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


app.include_router(router)


active_connections = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            for conn in active_connections:
                await conn.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)


@app.get("/external-data")
async def external_data():
    return await fetch_external_data()

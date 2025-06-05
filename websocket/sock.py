from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket : WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello Client !!")
    await websocket.receive_text()
    await websocket.close()


@app.websocket("/chat")
async def chat_endpoint(websocket : WebSocket):
    await websocket.accept()

    while True:
        message = await websocket.receive_text()
        await websocket.send_text(f"Received Message : {message}")



active_connection = []

@app.websocket("/broadcast")
async def broadcast_endpoint(websocket : WebSocket):
    await websocket.accept()
    active_connection.append(websocket)

    try : 
        while True:
            message = await websocket.receive_text()
            for connection in active_connection:
                if connection != websocket:
                    await connection.send_text(f"Broadcast Message : {message}")
    except Exception as e:
        print(f"Error : {e}")
        active_connection.remove(websocket)
    
    finally :
        if websocket in active_connection:
            active_connection.remove(websocket)
        await websocket.close()
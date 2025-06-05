from fastapi  import  FastAPI , WebSocket , WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections = {}
    
    #connect
    async def connect(self, websocket : WebSocket , username : str):
        await websocket.accept()
        self.active_connections[websocket] = username 

        await self.broadcast(f"+ {username} has joined")


    #disconnect all

    async def disconnect_all(self):        
        connections = list(self.active_connections.keys())
        for connection in connections:
            await connection.close()
            self.active_connections.pop(connection, None)

    #disconnect
    async def disconnect(self, websocket : WebSocket):
        if websocket in self.active_connections:
            username = self.active_connections.pop(websocket)
            await self.broadcast(f"- {username} has left")
            

            if username.lower() == "admin":
                await self.broadcast("Admin has disconnected the chat")
                await self.disconnect_all()
            
    #broadcast
    async def broadcast(self, message : str):
        disconnected_clients = []
        
        for connection in self.active_connections.keys():
            try:
                await connection.send_text(message)
            except:
                disconnected_clients.append(connection)
        
        for connection in disconnected_clients:
            self.active_connections.pop(connection, None)


manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket : WebSocket , username : str):
    await manager.connect(websocket, username)
    
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{username}: {data}")
            
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
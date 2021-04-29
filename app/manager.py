
from fastapi import WebSocket


class ConnectionManager:

	def __init__(self):
		self.connections = []

	async def connect(self, websocket: WebSocket):
		await websocket.accept()
		self.connections.append(websocket)

	async def broadcast(self, message: str):
		for con in self.connections:
			await con.send_text(message)


manager = ConnectionManager()

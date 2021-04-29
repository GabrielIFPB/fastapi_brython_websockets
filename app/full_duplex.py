
from typing import Dict

from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.manager import manager

full_duplex_router = APIRouter()
templates = Jinja2Templates(directory='templates')


class Message(BaseModel):
	message: str


@full_duplex_router.get('/page-full-duplex', response_class=HTMLResponse)
def route(request: Request):
	return templates.TemplateResponse(
		'full-duplex.html', {'request': request}
	)


@full_duplex_router.post('/page-full-duplex/data', response_model=Message)
async def route_data(message: Message) -> Dict[str, str]:
	await manager.broadcast(message.message)
	return {'message': 'ok'}


@full_duplex_router.websocket('/ws/full-duplex/{user}')
async def endpoint(websocket: WebSocket):
	await manager.connect(websocket)
	try:
		while True:
			data = await websocket.receive_text()
			await manager.broadcast(data)
	except WebSocketDisconnect:
		manager.disconnect(websocket)

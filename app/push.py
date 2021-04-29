
from typing import Dict

from fastapi import APIRouter, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.manager import manager

push_router = APIRouter()
templates = Jinja2Templates(directory='templates')


class Message(BaseModel):
	message: str


@push_router.get('/page-push', response_class=HTMLResponse)
def route(request: Request):
	return templates.TemplateResponse(
		'push.html', {'request': request}
	)


@push_router.post('/page-push/data', response_model=Message)
async def route_data(message: Message) -> Dict[str, str]:
	await manager.broadcast(message.message)
	return {'message': 'ok'}


@push_router.websocket('/ws/push')
async def push_endpoint(websocket: WebSocket):
	await manager.connect(websocket)
	while True:
		data = await websocket.receive_text()
		await manager.broadcast(data)

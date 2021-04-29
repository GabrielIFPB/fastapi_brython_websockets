
from typing import Dict

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

dynamic_router = APIRouter()
templates = Jinja2Templates(directory='templates')


class Message(BaseModel):
	message: str


@dynamic_router.get('/page-dynamic', response_class=HTMLResponse)
def route(request: Request):
	return templates.TemplateResponse(
		'dynamic.html', {'request': request}
	)


@dynamic_router.get('/page-dynamic/data', response_model=Message)
def route_data(request: Request) -> Dict[str, int]:
	from random import randint
	return {"message": randint(1, 100)}


@dynamic_router.get('/polling', response_class=HTMLResponse)
def polling(request: Request):
	return templates.TemplateResponse(
		'polling.html', {'request': request}
	)

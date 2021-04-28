
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

static_router = APIRouter()
templates = Jinja2Templates(directory='templates')


@static_router.get('/page-static', response_class=HTMLResponse)
def route(request: Request):
	return templates.TemplateResponse(
		'static.html',
		{'request': request}
	)

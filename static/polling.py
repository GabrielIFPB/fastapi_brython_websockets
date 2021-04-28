
from browser import ajax, bind, document, html, timer


def on_complete(request):
	document['response'] <= html.P(request.text)


def request_simulation():
	ajax.get('/page-dynamic/data', oncomplete=on_complete)
	timer.set_timeout(request_simulation, 2000)


request_simulation()

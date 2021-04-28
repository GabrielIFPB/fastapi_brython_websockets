
from browser import ajax, bind, document, html


def on_complete(request):
	document['response'] <= html.P(request.text)


@bind('#button', 'click')
def click_button(event):
	ajax.get('/page-dynamic/data', oncomplete=on_complete)

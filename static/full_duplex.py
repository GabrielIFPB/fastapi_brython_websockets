
from browser import prompt, websocket, window, document, html, bind

name = prompt('Enter your name ')

ws = websocket.WebSocket(f'ws://{window.location.host}/ws/full-duplex/{name}')


@bind('#send', 'click')
def send(event):
	ws.send(f'{name} disse: {document["text"].value}')
	document["text"].value = ''


def on_open(event):
	ws.send(f'{name}, Entrou na sala.')


def on_message(event):
	messages = document['messages']
	messages <= html.P(event.data)
	messages.scrollTop = messages.scrollHeight - messages.clientHeight


ws.bind('open', on_open)
ws.bind('message', on_message)

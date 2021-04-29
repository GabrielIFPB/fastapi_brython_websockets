
from browser import websocket, window, document


def on_open(event):
	print('connected')


def on_message(event):
	print('connected')
	document['message'].textContent = event.data


ws = websocket.WebSocket(f'ws://{window.location.host}/ws/push')
ws.bind('open', on_open)
ws.bind('message', on_message)

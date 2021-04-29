
"""
teste full duplex
"""
import asyncio
from websockets import connect


async def send(message):
	uri = "ws://localhost:8000/ws/full-duplex/gabriel"
	async with connect(uri) as ws:
		await ws.send(message)
		print(await ws.recv())

# asyncio.run(send("teste"))
# for x in range(100):
# 	asyncio.run(send(f"sem o browser: {str(x)}"))


async def hello():
	uri = "ws://localhost:8000/ws/full-duplex/dell"
	async with connect(uri) as ws:
		while True:
			message = await ws.recv()
			print(message)


def execute():
	asyncio.run(hello())

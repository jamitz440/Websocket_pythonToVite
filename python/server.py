import asyncio
import websockets
import json

count = False


async def send_numbers(websocket):
    global count
    while True:
        if count:
            for number in range(1, 11):
                if not count:
                    break
                message = json.dumps({"type": "number", "data": number})
                await websocket.send(message)
                await asyncio.sleep(0.01)  # Set very quick to test the speed.
        else:
            await asyncio.sleep(1)  # set to one second to not slow it down too much


async def receive_messages(websocket):
    global count
    async for message in websocket:
        print(f"Received message: {message}")
        data = json.loads(message)
        if data["type"] == "echo":
            await websocket.send(json.dumps({"type": "echo", "data": data["data"]}))
        if data["type"] == "button":
            if data["data"] == "start":
                doThink()
                count = True
            elif data["data"] == "stop":
                count = False
            print("button pressed")
            await websocket.send(
                json.dumps(
                    {"type": "echo", "data": (data["data"]).title() + " Button Pressed"}
                )
            )


async def handler(websocket, path):
    print(path)
    # asyncio.gather allows them to be sent/received concurrently
    await asyncio.gather(send_numbers(websocket), receive_messages(websocket))


def doThink():
    print("done thing")


start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

import asyncio
import websockets
import json

count = False


async def send_numbers(websocket):
    number = input("what number should i send? ")
    message = json.dumps({"type": "number", "data": number})
    await websocket.send(message)


async def receive_messages(websocket):
    global count
    async for message in websocket:
        print(f"Received message: {message}")
        data = json.loads(message)
        if data["type"] == "echo":
            await websocket.send(json.dumps({"type": "echo", "data": data["data"]}))
        if data["type"] == "button":
            if data["data"] == "start":
                await send_numbers(websocket)
            elif data["data"] == "stop":
                doThink()
            print("button pressed")
            await websocket.send(
                json.dumps(
                    {"type": "echo", "data": (data["data"]).title() + " Button Pressed"}
                )
            )


async def handler(websocket, path):
    print(path)
    # asyncio.gather allows them to be sent/received concurrently
    await asyncio.gather(receive_messages(websocket))


def doThink():
    print("done thing")


start_server = websockets.serve(handler, "localhost", 3456)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

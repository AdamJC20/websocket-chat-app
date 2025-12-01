import asyncio
import websockets


async def async_input(prompt: str = ""):
    # Run input() in a thread so it doesn’t block the event loop
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input, prompt)


async def client():
    async with websockets.connect("ws://localhost:8765") as websocket:

        async def listen():
            async for message in websocket:
                print(f"\n[received] {message}")

        async def send():
            while True:
                msg = await async_input("> ")
                await websocket.send(msg)

        await asyncio.gather(listen(), send())

asyncio.run(client())

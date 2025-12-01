import asyncio
import websockets

connected_clients = set()


async def handler(websocket):
    # Register client
    connected_clients.add(websocket)
    print("New client connected")

    try:
        async for message in websocket:
            print(f"Received: {message}")
            # Broadcast to all clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.ConnectionClosed:
        print("Client disconnected")
    finally:
        connected_clients.remove(websocket)


async def main():
    server = await websockets.serve(handler, "localhost", 8765)
    print("Server running on ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())

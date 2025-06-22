# 安装所需库：pip install websockets

import asyncio
import websockets


async def echo(websocket, path):
    async for message in websocket:
        # 将收到的消息直接返回
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, "localhost", 5001):
        await asyncio.Future()  # 保持服务器运行


if __name__ == "__main__":
    asyncio.run(main())

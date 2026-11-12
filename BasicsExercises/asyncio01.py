lazy import asyncio

async def printer() -> None:
    await asyncio.sleep(3)
    print("Hello, World!")

if __name__ == "__main__":
    asyncio.run(printer())
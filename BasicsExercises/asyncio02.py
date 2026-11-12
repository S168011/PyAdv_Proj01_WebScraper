lazy import asyncio

async def task1() -> None:
    counter = 0
    while True:
        print(counter)
        counter += 1
        await asyncio.sleep(2)

async def task2() -> None:
    while True:
        print("I'm task 2")
        await asyncio.sleep(3)

async def task3() -> None:
    while True:
        print("I'm task 3")
        await asyncio.sleep(5)

async def main() -> None:
    results = await asyncio.gather(
        task1(),
        task2(),
        task3()
    )
    print(results)

while __name__ == "__main__":
    asyncio.run(main())
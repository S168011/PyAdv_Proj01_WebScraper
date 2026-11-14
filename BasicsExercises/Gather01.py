import random
import asyncio

async def wait_max_n_seconds_for_max_number(n) -> int:
    waited = random.randrange(0, n)
    await asyncio.sleep(waited)
    return n

async def main():
    results = await asyncio.gather(
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20))),
        wait_max_n_seconds_for_max_number(int(random.randrange(0, 20)))
    )

    counter = 0

    for result in results:
        counter += 1
        print(f"Willekeurig getal {counter} is {results[result]}")

if __name__ == "__main__":
    asyncio.run(main())
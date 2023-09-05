import asyncio


async def generate(num: int) -> int:
    await asyncio.sleep(num)
    print(f'Корутина generate с аргументом {num}')

async def main():
    tasks = [generate(_) for _ in range(10)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
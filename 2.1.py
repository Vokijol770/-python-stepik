import asyncio


async def main():
    print('Hello, world!')
    await asyncio.sleep(1)
    print('World!')


if __name__ == '__main__':
    asyncio.run(main())
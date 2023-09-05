import asyncio


async def coro_1():
    await asyncio.sleep(1)
    print('coro_1 says, hello coro_2!')


async def coro_2():
    await asyncio.sleep(1)
    print('coro_2 says, hello coro_1!')


async def main():
    coro1 = coro_1()
    coro2 = coro_2()
    await asyncio.gather(coro1, coro2)


if __name__ == '__main__':
    asyncio.run(main())

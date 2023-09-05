import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Привет из корутины task1")

async def task2():
    await asyncio.sleep(1)
    print("Привет из корутины task2")

async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    await asyncio.gather(task_1, task_2)

asyncio.run(main())

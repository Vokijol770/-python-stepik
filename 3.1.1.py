import asyncio

#  Определение корутины
async def my_coroutine():
    print("Запуск корутины")
    await asyncio.sleep(10)  # Приостановка корутины на 1 секунду
    print("Завершение корутины")

async def my_coroutine2():
    for _ in range(1000):
        print(_, end=' ')

    print()


#  Создание задачи из корутины
async def main():
    task = asyncio.create_task(my_coroutine())
    task1 = asyncio.create_task(my_coroutine2())
    await task
    await task1

#  Запуск event loop
asyncio.run(main())

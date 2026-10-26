import asyncio


async def task1():
    print("Task1: started")
    await asyncio.sleep(2)
    print("Task1: completed")


async def task2():
    print("Task2: started")
    await asyncio.sleep(2)
    print("Task2: completed")


async def main():
    await asyncio.gather(task1(), task2())


asyncio.run(main())

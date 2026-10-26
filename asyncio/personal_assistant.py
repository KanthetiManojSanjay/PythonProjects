import asyncio


async def fetch_weather():
    print("fetch_weather: started")
    await asyncio.sleep(2)
    print("fetch_weather: completed")


async def fetch_stock_price():
    print("fetch_stock_price: started")
    await asyncio.sleep(3)
    print("fetch_stock_price: completed")


async def main():
    await asyncio.gather(task1(), task2())


asyncio.run(main())

import asyncio, time

async def func1():
    await asyncio.sleep(5)
    return True

async def func2():
    await asyncio.sleep(5)
    return True

async def func3():
    await asyncio.sleep(5)
    return True

async def main():
    await asyncio.gather(func1(), func2(), func3())
    # await func1()
    # await func2()
    # await func3()
    return True

start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()
print (end - start)
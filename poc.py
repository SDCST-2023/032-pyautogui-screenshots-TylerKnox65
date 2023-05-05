import asyncio
from typing import Counter

c = 0

async def task1():
    global c
    while True:
        print("task1".ljust(30))
        c+= 1
        await asyncio.sleep(0.001)

async def task2():
    global c
    while True:
        c+=1
        print("task2".center(30))
        await asyncio.sleep(0.01)

async def task3():
    while True:
        print("task3".rjust(30),c)
        await asyncio.sleep(0.1)  

async def main():
    tasks = []
    tasks.append( asyncio.create_task(task1() ))
    tasks.append( asyncio.create_task(task2() ))
    tasks.append( asyncio.create_task(task3() ))
    for i in tasks:
        await i



asyncio.run( main() )
import time
import asyncio
from asyncio import gather
from random import randint


# დავალება 1.
#
# დაწერეთ ორი ასინქრონული ფუნქცია, ერთ-ერთი დააყოვნეთ 2 წამი, მეორე 5 წამი,
# დაბეჭდეთ მათი დაწყება და დასრულება, თასქები შექმენით ცალ-ცალკე და გაუშვით.
#


async def open_door():
    print("the door is being opened")
    await asyncio.sleep(2)
    print("the door is being closed")


async def fix_issue():
    print("the issue is being fixed")
    await asyncio.sleep(5)
    print("fixed")


async def main():
    start_time = time.time()

    result = asyncio.gather(open_door(), fix_issue())
    task1, task2 = await result

    end_time = time.time()
    delta = end_time - start_time
    print(f"it took {delta} seconds")

if __name__ == "__main__":
    asyncio.run(main())



# დავალება 2.
#
# დაწერეთ ასინქრონული ფუნქცია, რომელიც რენდომად არჩეული დროით დააყოვნებს და
# დაბეჭდავს რიცხვებს 1-დან 10-მდე


import random


async def print_colors():
    random_num = randint(1, 5)

    print(f"random number is {random_num}")
    await asyncio.sleep(random_num)
    print(f"i slept for {random_num} seconds")


async def main():
    start_time = time.time()

    result = await asyncio.gather(print_colors())


    end_time = time.time()
    delta = end_time - start_time
    print(f"it took {delta} seconds")


if __name__ == "__main__":
    asyncio.run(main())


# დავალება 3.
#
# დაწერეთ ასინქრონული ფუნქცია, დააბრუნებს ატრიბუტად გადაწოდებული რიცხვის კვადრატს,
# იმ შემთხვევაში თუ ეს რიცხვი არის ლუწი, ამის შესამოწმებლად დაწერეთ მეორე ასინქრონული ფუნქცია.
# შესამოწმებლად შექმენით რამდენიმე თასქი, გამოიყენეთ gather მეთოდი



async def is_even(number):
    await asyncio.sleep(1)
    return number % 2 == 0



async def square_if_even(number):
    if await is_even(number):
        return number ** 2
    else:
        return f"{number} არ არის ლუწი"



async def main():
    numbers = [1, 2, 3, 40, 50]
    tasks = [square_if_even(num) for num in numbers]


    results = await asyncio.gather(*tasks)
    print(results)



if __name__ == "__main__":
    asyncio.run(main())


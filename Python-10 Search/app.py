# დავალება 1.

# დაწერეთ პითონის ფუნქცია რომელიც დააგენერირებს 100 შემთხვევითობის
# პრინციპით არჩეული რიცხვებით შევსებულ ლისტს.

# დაწერეთ ფუნქცია, რომელიც ხაზობრივი ძიების გამოყენებით მოიძიებს
# მოცემულ ლისტში რომელიმე ელემენტს.

# გამოიყენეთ ერთ-ერთი სორტირების ალგორითმი და დასორტირებულ სიაში
# ელემენტის ძიებისთვის დაწერეთ ბინარული ძიება.

import random


def random_number_list():
    list_1 = []
    for _ in range(100):
        random_number = random.randint(0, 100)
        list_1.append(random_number)

    return list_1


def search():
    list_of_numbers = random_number_list()
    search_value = random.randint(0, 110)
    print(search_value)
    for index, number in enumerate(list_of_numbers):
        if number == search_value:
            return f"index {index}, number {number}"
    return -1


print(search())


new_list = random_number_list()
new_list.sort()
print(new_list)


def search(lst, x):
    low = 0
    high = len(lst)-1

    while low <= high:
        mid = (low+high) // 2
        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1


print(search(new_list, 5))

# დავალება 2.

# დაწერეთ ლამბდა ფუნქცია, რომელიც დააბრუნებს სამის ჯერად რიცხვებს,
# ამის შემდეგ დაწერეთ ფუნქცია, რომელსაც ატრიბუტებად გადაეწოდება ლისტი
# და ლამბდა ფუნქცია, ხაზობრივი ძიების და ლამბდა ფუნქციის დახმარებით შეავსეთ
# ახალი ლისტი(ინდექსებით) და დააბრუნეთ მოცემული ლისტი.(ფუნქციამ უნდა დააბრუნოს
#  ლისტი, რომელშიც შენახული იქნება სამის ჯერადი რიცხვების ინდექსები)


def division_by_three(item): return item % 3 == 0


random_list = [7, 10, 15, 20, 30, 40, 50, 60, 70, 80, 77, 33, 85]


def test(lst, division_by_three):
    new_list = []
    for index, item in enumerate(lst):
        if division_by_three(item):
            new_list.append(index)

    return new_list


print(test(random_list, division_by_three))

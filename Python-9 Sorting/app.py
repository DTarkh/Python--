# დავალება 1.

# დაწერეთ ფუნქცია, რომელიც დააგენერირებს 100 შემთხვევითობის
# პრინციპით დაგენერირებული ელემენტისგან შემდგარ ლისტს, გამოიყენეთ
# sort() მეთოდი და sorted() ფუნქცია, დააბრუნეთ დასორტირებული ლისტი
# ჯერ ზრდადობით და შემდეგ კლებადობით


import random

# def sorting():
#     random_list = []

#     for _ in range(100):
#         random_number = random.randint(0,100)
#         random_list.append(random_number)

#     sorted_list = sorted(random_list)
#     sorted_list_reversed = sorted(random_list, reverse=True)

#     return sorted_list, sorted_list_reversed


# print(sorting())


# დავალება 2.

# დაწერეთ ფუნქცია, რომელიც დააგენერირებს 100 შემთხვევითობის პრინციპით
# დაგენერირებული ელემენტისგან შემდგარ ლისტს, გამოიყენეთ ორი სორტირების
# ალგორითმი(არ აქვს არსებითი მნიშვნელობა, რომელი ალგორითმები იქნება),
# ერთი ალგორითმით დაასორტირეთ ზრდადობით, მეორე ალგორითმით დაასორტირეთ კლებადობით,
# ორივე შედეგი დაპრინტეთ ტერმინალში.


# def buble_sorter():
#     random_list = []

#     for _ in range(100):
#         random_number = random.randint(0, 100)
#         random_list.append(random_number)

#     for i in range(len(random_list)):
#         swapped = False
#         for j in range(len(random_list)-1):
#             if random_list[j] > random_list[j+1]:
#                 random_list[j], random_list[j +
#                                             1] = random_list[j+1], random_list[j]
#                 swapped = True

#         if swapped == False:
#             break

#     return random_list


# def selection_sorting():

#     random_list2 = []

#     for _ in range(100):
#         random_number2 = random.randint(0, 100)
#         random_list2.append(random_number2)

#     for i in range(len(random_list2)):
#         min_index = i
#         for j in range(i+1, len(random_list2)):
#             if random_list2[j] > random_list2[min_index]:
#                 min_index = j

#         random_list2[i], random_list2[min_index] = random_list2[min_index], random_list2[i]

#     return random_list2


# print(buble_sorter())
# print(selection_sorting())

# დავალება 3.

# ქალაქში მოსახლეობის რაოდენობა ყოველ წელს იზრდება 2 პროცენტით.

# 1.დაწერეთ ფუნქცია რომელიც გამოთვლის, რამდენი წლის შემდეგ იქნება
# მოსახლეობა 10000 ადამიანზე მეტი.

# 2. დაწერეთ ფუნქცია რომელიც ატრიბუტად მიიღებს წლების რაოდენობას,
#  დააბრუნეთ მოსახლეობის რაოდენობა ამდენი წლის შემდეგ.


# def count_years(target_population, initial_population=3000, growth_rate=0.2):
#     years = 0

#     current_population = initial_population

#     while current_population <= target_population:
#         current_population += current_population * growth_rate
#         years += 1

#     return years

# print(count_years(10000))


# def count_population(years, initial_population=3000, growth_rate=0.2):


#     for i in range(years):
#         initial_population += initial_population * growth_rate

#     return initial_population


# print(count_population(7))


# დავალება 4.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს 2, ინტეჯერებისგან შემდგარ,
#  ლისტს, შეადარეთ ერთი და იგივე ადგილზე მდგომი ელემენტები და დააბრუნეთ
# ახალი ლისტი, რომელშიც მოცემული იქნება შედარების შედეგად მიღებული მაღალი რიცხვები. დაამატეთ ლოგიკური გამონაკლისი შემთხვევები.


# def compare(list1, list2):
#     new_list = []

#     if len(list1) >= len(list2):
#         for i in range(list1):
#             if list1[i] > list2[i]:
#                 new_list.append(list1[i])
#             elif list2[i] > list1[i]:
#                 new_list.append(list2[i])

#     if len(list1) <= len(list2):
#         for i in range(list2):
#             if list1[i] > list2[i]:
#                 new_list.append(list1[i])
#             elif list2[i] > list1[i]:
#                 new_list.append(list2[i])

#     return new_list


# list1 = [3, 4, 5, 6, 7, 8]
# list2 = [1, 2, 3, 4, 5, 6]

# print(compare(list1, list2))


# დავალება 5.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს 3 რიცხვს, ფუნქციას დააბრუნებინეთ
# პასუხი, არის თუ არა შესაძლებელი ამ რიცხვებით სამკუთხედის აგება.
# სამკუთხედის ორი გვერდის ჯამი, მეტია მესამე გვერდზე

# def triangle(num1,num2,num3):
#     if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
#         return True
#     else:
#         return False


# num1 = 10
# num2 = 15
# num3 = 20

# print(triangle(num1,num2,num3))


# დავალება 6.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს სტუდენტების ლისტს,
student_list = [
    '1 - Melissa Parker - 91 60 89 84 26',
    '2 - Paige Simon - 39 90 38 74 49',
    '3 - Kevin Atkins - 27 7 89 96 62',
    '4 - Barry Ramos - 94 93 62 30 66',
    '5 - Karen Hudson - 51 15 94 20 8',
    '6 - Jennifer Diaz - 56 31 81 52 50',
    '7 - Robin Smith - 90 3 92 86 14',
    '8 - Kevin Clark - 69 65 47 58 44',
    '9 - Lisa Shields DDS - 92 1 53 40 89',
    '10 - John Kennedy - 21 41 12 15 90',
]

# გამოთვალეთ თითოეული სტუდენტისთვის საშუალო ქულა და დააბრუნებინეთ ფუნქციას ლისტის სახით,
# [[name, avg], [name, avg] …]


# def average(list_one):
#     result = []
#     for student in student_list:
#         splitted = student.split(' - ')
#         result.append(splitted)
#     # print(result)

#     final_list = []

#     for student in result:
#         name = student[1]
#         grades = student[2].split()

#         sum_grades = 0
#         for grade in grades:
#             sum_grades += int(grade)
#             avg_grades = sum_grades / len(grades)

#         final_list.append([name, avg_grades])

#     return (final_list)


# list_one = student_list
# print(average(list_one))


# დავალება 7.

# დაწერეთ ფუნქცია, რომელსაც ატრიბუტად გადაეწოდება ლისტი:
# [9255, 1358, 1045285, 59828218, 881525, 388, 8586, 9988, 599828, 812358, 855, 85585, 85885, 888]

# დააბრუნეთ ახალი ლისტი, რომელიც შედგება რიცხვებისგან:
# 	შეიცავს 5, 8 ციფრებს
# 	ციფრი 8-ს რაოდენობა არის 5-ის რაოდენობაზე მეტი

# new_list = [9255, 1358, 1045285, 59828218, 881525, 388, 8586, 9988, 599828, 812358, 855, 85585, 85885, 888]

# def filter_list(list_one):


#     my_list = []

#     for i in list_one:
#         turn_to_string = str(i)
#         count_5 = turn_to_string.count('5')
#         count_8 = turn_to_string.count('8')
#         if '5' in turn_to_string and '8' in turn_to_string and count_8 > count_5:
#             my_list.append(i)


#     return my_list

# print(filter_list(new_list))

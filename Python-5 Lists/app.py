
# დავალება 1.

# მოცემულია სია my_list:
# mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
# დაწერეთ პროგრამა, რომელიც შეკრებს ამ სიის მე–3, მე–9 და მე–14
# ელემენტებს და მიღებულ შედეგ დაბეჭდავს ტერმინალში.

# mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]

# first_number = mylist[2]
# second_number = mylist[8]
# third_number = mylist[13]
# print(first_number, second_number, third_number)

# sumarry = first_number + second_number + third_number

# print(f"Sum of this numbers is {sumarry}")


# დავალება 2.

# შექმენით 20 რენდომ რიცხვისგან შემდგარი ლისტი, შექმენით ახალი ლისტი,
# რომელშიც შეინახავთ პირველი ლისტიდან მხოლოდ კენტ მნიშვნელობებს და
# დაბეჭდეთ ლისტში ყველაზე მცირე და ყველაზე დიდი ელემენტი. არ გამოიყენოთ
#  ფუნქციები min() და max()

# import random

# numbers_list = []

# for i in range(20):
#     random_numbers = random.randint(1, 100)
#     if random_numbers % 2 != 0:
#         numbers_list.append(random_numbers)


# numbers_list.sort()
# print(f"Min number is: {numbers_list[0]} and max number is: {numbers_list[-1]}")


# დავალება 3.

# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ლისტს my_llist = [43, '22', 12, 66, 210, ["hi"]],
#  და შეასრულებს
# შემდეგ ნაბიჯებს:
# a. დაბეჭდავს 210-ის ინდექს, თუ მერამდენე ინდექსზეა
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello"
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს ლისტს
# d. შექმენით ახალი ლისტი my_llist_2 , რომელსაც ექნება my_llist მნიშვნელობა, გაასუფთავეთ my_llist_2
# მნიშნველობა და დაბეჭდეთ my_llist და my_llist_2 ლისტები


# my_llist = [43, '22', 12, 66, 210, ["hi"]]

# print(my_llist.index(210))
# my_llist.append("hello")
# print(my_llist)
# my_llist.pop(2)
# print(my_llist)

# my_llist_2 = my_llist.copy()
# my_llist.clear()

# print(my_llist)
# print(my_llist_2)


# დავალება 4.

# დაწერეთ პროგრამა, რომელიც დაბეჭდავს ორი მატრიცის ჯამს, ჯამი გამოითვლება შემდეგი წესით,
#  ერთი და იგივე ადგილზე მდგომი ელემენტები ემატება ერთმანეთს, მატრიცების განზომილებები
#  უნდა იყოს ერთი და იგივე

# matrix_one = [[1, 2, 3], [4, 5, 6]]
# matrix_two = [[7, 8, 9], [10, 11, 12]]

# new_matrix = [[],[]]


# for i in range(len(matrix_one)):
#     for j in range(len(matrix_one[0])):
#          matrix_sum = matrix_one[i][j] + matrix_two[i][j]
#          print(matrix_sum)
#          new_matrix[i].append(matrix_sum)


# print(new_matrix)


# დავალება 5.

# დაწერეთ პროგრამა რომელიც გააკეთებს კვადრატული 3x3 მატრიცის ტრანსპონირებას, ტრანსპონირება ნიშნავს
# ინდექსების შებრუნებას, მაგ. თუ გვაქვს ერთ-ერთი ჩანაწერი ინდექსით list[2][3], ტრანსპონირების შემდეგ
# მისი ინდექსი უნდა გახდეს list[3][2], ასე ხდება ყველა ჩანაწერზე


# მაგ: [1, 2, 3]
#          [4, 5, 6]
#          [7, 8, 9]


# ტრანსპონირებული: [1, 4, 7]
#                                            [2, 5, 8]
#                                            [3, 6, 9]


# დავალება 6.

# list comprehension გამოყენებით შექმენით რენდომ რიცხვებისგან შემდგარი 4x4 კვადრატული მატრიცა

import random



matrix = [random.randint(1, 10) for i in range(4)] for j in range(4)[
for row in matrix:
    print(row)
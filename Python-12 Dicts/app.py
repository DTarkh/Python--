# დავალება 1.

# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს წინადადება,
# პროგრამას დააბეჭდინეთ დიქტის სახით რამდენჯერ არის თითოეული სიტყვა გამოყენებული წინადადებაში

# input: The wind howled and howled all night long
# output: {“the”: 1, “wind”:1, “howled”:2, “and”:1, “all”:1, ”night”:1, “long”:1}


# sentence = input("Enter the sentence: ")

# words = sentence.lower().split()
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)


# დავალება 2.

# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ორი რიცხვი და ერთი მათემატიკური ოპერატორი,
# ააწყვეთ კალკულატორი, რომელიც გამოთვლის შესაბამის მოქმედებას, გამოიყენეთ დიქტები, სადაც key მნიშვნელობებად
# იქნება მათემატიკური ოპერატორები


# def add(first_number, second_number):
#     return first_number + second_number


# def sub(first_number, second_number):
#     return first_number - second_number


# def mul(first_number, second_number):
#     return first_number * second_number


# def div(first_number, second_number):
#     if second_number != 0:
#         return first_number / second_number
#     else:
#         return "can not divide by zero"


# math_operators = {"+": add, "-": sub, "*": mul, "/": div}

# first_number = input("Enter the frist number: ")
# second_number = input("Enter the second number: ")
# math_operator = input("Enter the match operator: ")

# if math_operator in math_operators:
#     result = math_operators[math_operator](first_number, second_number)
#     print(f"The result of {first_number} {math_operator} {second_number} is {result}")
# else:
#     print("Invalid math operator. Please enter a valid operator (+, -, *, /).")


# დავალება 3.

# comperhension-ის გამოყენებით დააგენერირეთ დიქტი, რომლის key მნიშვნელობები იქნება 1-დან 10-ის ჩათვლით რიცხვები,
#  ხოლო value მათი კვადრატი

# new_dict = {x: x*x for x in range(1, 11)}
# print(new_dict)

# დავალება 4.

# შექმენით დიქტი, რომელიც ინახავს ინფორმაციას დეპარტამენტების და თანამშრომლების შესახებ, თითოეულ თანამშრომელს
# უნდა ჰქონდეს ატრიბუტები: სახელი, გვარი, ასაკი, ხელფასი. გამოთვალეთ საშუალო ხელფასი დეპარტამენტების მიხედვით.


departments = {'department1': {'employee1': {'name': "john", 'surname': "doe", 'age': 28, 'salary': 1000}},
               'department2': {'employee2': {'name': "john", 'surname': "doe", 'age': 28, 'salary': 1200}},
               'department3': {'employee3': {'name': "john", 'surname': "doe", 'age': 28, 'salary': 1300}}
               }


# def av_salary(departments):
#     average_salaries = {}
#     for department, employees in departments.items():
#         total_salary = sum(employee['salary'] for employee in employees.values())
#         average_salary = total_salary / len(employees)
#         average_salaries[department] = average_salary

#     return average_salaries

# print(av_salary(departments))

# დავალება 5.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს დიქტს, ფუნქციამ უნდა დააბრუნოს შებრუნებული დიქტი, სადაც key
# მნიშვნელობები იქნება ორიგინალი დიქტის value და value იქნება ორიგინალი დიქტის key მნიშვნელობები


def reverse_key_value(dictionary):
    reversed_dict = {value: key for key, value in dictionary.items()}
    return reversed_dict


dictonary = {"a": 1, "b": 2, "c": 3}

print(reverse_key_value(dictonary))

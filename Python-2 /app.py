# დავალება 1.
# დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას.
#  თუ რიცხვი ლუწია გამოიტანეთ ტექსტი ‘even’ თუ კენტია ‘odd’

# number = int(input('enter number: '))

# if number % 2 == 0:
#     print("even")
# else:
#     print("even")


# დავალება 2.
# დაწერეთ პროგრამა რომელიც მომხმარებლის მიერ შეყვანილ ტექსტში მოძებნის სიტყვებს “small”, “tall”, “middle”

# 	a. თუ ტექსტში აღმოჩნდება რომელიმე მათგანი, დაბეჭდეთ სიტყვა

# 	b. თუ ტექსტში არცერთი სიტყვა მოიძებნა დაბეჭდეთ, რომ ტექსტში ეს 	სამი სიტყვა არ მოიძებნა


# user_input = input('enter text: ')


# if "small" in user_input:
#     print("small")
# if "tall" in user_input:
#     print("tall")
# if "middle" in user_input:
#     print("middle")

# if "small" not in user_input and "tall" not in user_input and "middle" not in user_input:
#     print("there are not words in the text.")


# დავალება 3.
# დაწერეთ კალკულატორი, რომელიც შეგვეკითხება პირველ რიცხვს, შემდეგ მეორე რიცხვს, შემდეგ მათემატიკურ ოპერატორს
# და შესაბამისი მათემატიკური ოპერატორის გამოყენებით დაგვიბეჭდავს შედეგს.


first_number = float(input("enter first number: "))
second_number = float(input("enter second number: "))
math_operator = input("enter math operator: ")


if math_operator == "+":
    print(first_number + second_number)
elif math_operator == "-":
    print(first_number - second_number)
elif math_operator == "*":
    print(first_number * second_number)
elif math_operator == "/":
    print(first_number / second_number)
elif math_operator == "**":
    print(first_number ** second_number)
elif math_operator == "//":
    print(first_number // second_number)
elif math_operator == "%":
    print(first_number % second_number)
else:
    print("wrong operator")

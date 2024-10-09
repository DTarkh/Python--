# დავალება 1.
# დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს ტექსტის შეყვანას და თუ შეყვანილი ტექსტი
# არის პალინდრომი დაბეჭდეთ “შეყვანილი ტექსტი არის პალინდრომი” თუ არა, მაშინ დაბეჭდეთ “შეყვანილი
# ტექსტი არ არის პალინდრომი”
# პალინდრომი არის ისეთი ტექსტი, რომელიც მარცხნიდანაც და მარჯვნიდანაც ერთნაირად იკითხება


# user_input = input('Enter word: "')
# reverse_input = user_input[::-1]
# print(reverse_input)

# if user_input == reverse_input:
#     print("The input is palindrome.")
# else:
#     print("The input is not palindrome.")


# დავალება 2.
# დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ტექსტი, ტექსტის სიმბოლოები გადაყავს
# შესაბამის ASCII სტანდარტში და გვიბეჭდავს ამ რიცხვების თანმიმდევრობას


user_input = input('Enter word: ')
for i in user_input:
    print(f"Letter {i}'s ASCII code is {ord(i)}")

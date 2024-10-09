
# დავალება1.
# დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდენ იყენებს while ციკლს,
# რომ რევერსულად დაბეჭდოს რიცხვები 0-მდე, მაგალითად თუ შეიყვანს რიცხვს 4, დაიბეჭდოს 4,3,2,1


# number = int(input("enter number:"))


# while number > 0:
#     print(number)
#     number -= 1
# else:
#     print("done")


# დავალება2.
# დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0,
# შეამოწმეთ რიცხვი, თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს, ეს პროცესი გაგრძელდეს მანამ,
# სანამ მომხმარებელი არ შეიყვანს ტექსტს sum, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.


# total_sum = 0

# while True:
#     brake_statement = input("for braking type \"sum\" to continue press enter ")
#     if  brake_statement == "sum":
#         print("Sum is:", total_sum)
#         break

#     number = int(input("enter number:"))
#     if number > 0:
#         total_sum += number


# დავალება3(არასავალდებულო).
# დაწერეთ პითონის პროგრამა, რომელიც შემთხვევითობის პრინციპით აირჩევს რიცხვს ნებისმიერ შუალედში, ასევე
# აირჩიეთ სიცოცხლეების რაოდენობა, რომელსაც შეინახავთ ცვლადში, პროგრამამ კი მომხმარებელს უნდა მოთხოვოს რიცხვის
# შეყვანა მანამ, სანამ არ წააგებს ან სანამ არ მოიგებს, თუ რიცხვს შევიყვანთ უფრო მაღალს, დაგვიბეჭდოს რომ რიცხვი
# მაღალია, თუ შევიყვანთ დაბალს დაგვიბეჭდოს რომ რიცხვი დაბალია.
# წაგების ან მოგების შემთხვევაში პროგრამა უნდა გაჩერდეს.

# გამოიყენეთ else ბლოკი while ციკლთან ერთად

from random import randint

random_number = randint(1, 20)
print(random_number)
life = 3

while life > 0:
    number = int(input("enter number: "))
    if number > random_number:
        print("bigger")
        life -= 1
    elif number < random_number:
        print("smaller")
        life -= 1
    elif number == random_number:
        print("you win")
        break

else:
    print("you lose")

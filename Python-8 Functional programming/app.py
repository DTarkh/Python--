# დავალება 1.

# დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი და
# იგივე ზომის სიას(list) და zip ფუნქციის გამოყენებით დააჯგუფეთ
# სიების ელემენტები ერთმანეთთან.
# params: [1, 2, 3], ['a', 'b', 'c']
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]


from functools import reduce
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

combined = zip(list1, list2)
print(list(combined))


# დავალება 2.

# დაწერეთ lambda ფუნქცია რომელიც იღებს სიას(list) და აბრუნებს მხოლოდ სიის
# ლუწ ელემენტებს
# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [2, 4, 6]


params = [1, 2, 3, 4, 5, 6, 7]
odd_number_list = [(lambda x=num: x if x % 2 == 0 else "odd")()
                   for num in params]

# იგივე ფილტრით

odd_number_list2 = list(filter(lambda x: x % 2 == 0, params))

# იგივე comperhension

odd_number_list3 = [num for num in params if num % 2 == 0]

print(odd_number_list)
print(odd_number_list2)
print(odd_number_list3)


# დავალება 3.

# დაწერეთ lambda ფუნქცია, რომელიც დააბრუნებს მხოლოდ რიცხვის დადებით მნიშვნელობებს,
# შესამოწმებელი რიცხვები აღწერილი უნდა იყოს ლისტში. გამოიყენეთ filter ფუნქცია functools
# მოდულიდან


list_one = [2, -4, -1, 5, 7, -52, 80, -3, 3]

positive_numbers_list = filter(lambda x: x > 0, list_one)

print(list(positive_numbers_list))


# დავალება 4.

# დაწერეთ lambda ფუნქცია, რომელიც პასუხად დააბრუნებს სტრინგი არის თუ არა პალინდრომი,
# სტრინგები უნდა იყოს შენახული ლისტში. დაწერეთ filter ფუნქციის გამოყენებით


string_one = ["tenet"]

is_palindrome = filter(lambda x: x == x[::-1], string_one)
print(list(is_palindrome))


# დავალება 5.

# დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების
# ნამრავლს, ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის
# პარამეტრს (TypeError). ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.
# params:[1, 2, 3, 4, 5]
# output: 120


list_one = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x * y, list_one))

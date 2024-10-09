
# დავალება 1.
# დაწერეთ პროგრამა, რომელიც კითხულობს სამ მთელ რიცხვს და ეკრანზე გამოაქვს მათი ჯამი.


# first_number = input("Enter first number: ")
# second_number = input("Enter second number: ")
# third_number = input("Enter third number: ")

# sum_number = int(first_number) + int(second_number)+ int(third_number)

# print(sum_number)


# დავალება 2.
# დაწერეთ პროგრამა, რომელიც კითხულობს კუბის გვერდის სიგრძეს (მთელი რიცხვი), გამოითვლის კუბის
# მოცულობას - V და ზედაპირის ფართობს - S და ამ ორ მონაცემს დაბეჭდავს ეკრანზე.


# cube_side_length = input("Cube side length: ")

# cube_volume = int(cube_side_length) ** 3

# print("Cume volume is:", cube_volume)

# cube_surface_area = int(cube_side_length) ** 2 * 6

# print("Cube surface area is:", cube_surface_area)


# დავალება 3.
# დაწერეთ პროგრამა, რომელიც ცალ-ცალკე კითხულობს კომპიუტერის შემადგენელი ნაწილების ფასებს -
# მონიტორის, სისტემური ბლოკის, კლავიატურის და მაუსის. ამ მონაცემების გამოყენებით გამოითვლის
# კომპიუტერის ფასს და დაბეჭდავს ეკრანზე.


monitor = input("What is the price of monitor?: ")
power_block = input("What is the price of the power block?: ")
keyboard = input("What is the price of the keyboard?: ")
mouse = input("What is the price of the mouse?: ")

sum_price = int(monitor) + int(power_block) + int(keyboard) + int(mouse)
print("Total price is:", sum_price)

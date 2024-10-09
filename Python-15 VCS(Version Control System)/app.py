# დავალება 1.

# დაწერეთ ფუნქცია, რომელიც წაიკითხავს ფაილს, დაბეჭდეთ ის ხაზები,
#  რომელიც არის ერთმანეთის პალინდრომი


# with open("test.txt", "w") as file:
#     write_text = file.write("tenet \n")
#     write_text = file.write("david \n")
#     write_text = file.write("ana")


# def read_file(filename):
#     with open(filename, 'r') as file:
#         lines = file.readlines()
#         found_palindrome = False
#         for line in lines:
#             line = line.strip()
#             if line == line[::-1]:
#                 print(f"{line} is a palindrome")
#                 found_palindrome = True

#         if not found_palindrome:
#             print("No palindrome found in the file")


# read_file("test.txt")

# დავალება 2.

# დაწერეთ პითონის ფუნქცია, რომელიც ატრიბუტად მიიღებს ფაილის სახელს,
#  წაიკითხეთ ფაილი, დაყავით ხაზები რაოდენობის მიხედვით და ჩაწერეთ ახალ
# ფაილებში, თითოში მაქსიმუმ 10 ხაზი.


import csv
with open("textline.txt", "w") as file:
    for line in range(1, 36):
        file.write(str(line) + "\n")


def func(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

        line_numbers = len(lines)

        num_files = (line_numbers // 10) + (1 if line_numbers % 10 != 0 else 0)

        for i in range(num_files):
            start_index = i * 10
            end_index = start_index + 10
            divide_lines = lines[start_index:end_index]

            output_filename = f"{file_name}_part{i + 1}.txt"
            with open(output_filename, 'w') as output_file:
                output_file.writelines(divide_lines)

            print(f"Created file: {output_filename}")


file_name = "textline.txt"
func(file_name)

# დავალება 3.

# დაწერეთ პითონის ფუნქცია, რომელიც ატრიბუტებად მიიღებს ფაილის სახელებს,
#  წაიკითხეთ ერთი ფაილი, ამოშალეთ ცარიელი ხაზები და სრული ინფორმაცია ჩაწერეთ მეორე ფაილში.


# with open("text_for_strip.txt", "w") as file:
#     write_text = file.write("tenet \n")
#     write_text = file.write("\n")
#     write_text = file.write("ana \n")
#     write_text = file.write("tenet jfelifjw jlwefljwf fljwejlfiwe \n")
#     write_text = file.write(" \n")
#     write_text = file.write("ana  ekf ilefl liwefiw \n")


# def strip_files(filename1, filename2):
#     with open(filename1, 'r') as file:
#         lines = file.readlines()

#     cleaned_lines = [line for line in lines if line.strip()]

#     with open(filename2, 'w') as file:
#         file.writelines(cleaned_lines)


# strip_files("text_for_strip.txt", "file_stripped.txt")


# with open("file_stripped.txt", "r") as file:
#     lines = file.readlines()


# დავალება 4.

# 1.# დაწერეთ პითონის აპლიკაცია რომელიც დასაწყისისთვის csv ფაილში ჩაწერს
# შემდეგ ინფორმაციას:
# [
#     {"title": "1984", "author": "George Orwell", "year": 1949},
#     {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
#     {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
#     {"title": "Moby Dick", "author": "Herman Melville", "year": 1851},
#     {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
#     {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
#     {"title": "Ulysses", "author": "James Joyce", "year": 1922},
#     {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
#     {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
#     {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
# ]


data = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "Moby Dick", "author": "Herman Melville", "year": 1851},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
    {"title": "Ulysses", "author": "James Joyce", "year": 1922},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]


def write_to_csv(filename):
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "author", "year"])
        writer.writeheader()
        writer.writerows(data)

    return data


# write_to_csv("data")


def read_and_add_to_csv():
    print(f"This is the following data: {write_to_csv("data")}")
    new_data = {}
    user_input_title = input("Enter title to data:")
    user_input_author = input("Enter author to data:")
    user_input_year = input("Enter year to data:")
    new_data["title"] = user_input_title
    new_data["author"] = user_input_author
    new_data["year"] = user_input_year
    with open("data", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "author", "year"])
        writer.writeheader()
        writer.writerows(data + [new_data])


# 2.# აღწერეთ ფუნქციები, წიგნის ინფორმაციის წაკითხვისათვის და ახალი
# ინფორმაციის დამატებისათვის.

# ამ ფუნქციის გამოძახების შემდეგ შევიყვანთ საჩირო ინფორმაციას,
# რაც დაემატება ჩვენს მიერ უკვე შექმნილ ფაილში

read_and_add_to_csv()


# 3.# მომხმარებელს მოთხოვეთ შეიყვანოს ინფორმაცია, სურს ინფორმაციის წაკითხვა
#  თუ ჩაწერა, წაკითხვის შემთხვევაში მოთხოვეთ სათაურის შეყვანა და ინფორმაცია
# მოიძიეთ ამ სათაურის მიხედვით.


read_or_write = input(
    "would you like to read or write information? type \"read\" or \"write\"")

if read_or_write == "read":
    type_of_info = input(
        "enter type of information to read(\"title\" ,\"author\" or \"year\")")
    if type_of_info == "title":
        with open("data", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row["title"])
    elif type_of_info == "author":
        with open("data", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row["author"])
    elif type_of_info == "year":
        with open("data", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row["year"])

if read_or_write == "write":
    read_and_add_to_csv()

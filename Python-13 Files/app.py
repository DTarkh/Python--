# დავალება 1.

# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ტექსტურ ფაილს და მასში ჩაწერს 1000
# ხაზს(ტექსტს არ აქვს მნიშვნელობა) თავისი ნუმერაციით, შემდეგ წაიკითხეთ ეს ფაილი
# და დაბეჭდეთ ხაზების რაოდენობა, თუ რამდენია შევსებული.


# new_file = open('text.txt', 'w')
# for i in range(1, 1001):
#     new_file.write(f'line {i}\n')

# new_file = open('text.txt', 'r')

# lines = new_file.readlines()
# print(f'Number of lines: {len(lines)}')

# new_file.close()


# დავალება 2.

# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ტექსტურ ფაილს და მეორე, მერვე, მეათე,
#  მეცამეტე და მეჩვიდმეტე ხაზებზე ჩაწერს ამ რიცხვებს შესაბამისი ტექსტური სახელით.


list_of_data = [
    (2, 'Two'),
    (8, 'Eight'),
    (10, 'Ten'),
    (13, 'Thirteen'),
    (17, 'Seventeen')
]

with open("numbers_with_names.txt", "w") as new_file:
    line_counter = 1
    max_line = max(line for line, _ in list_of_data)

    while line_counter <= max_line:
        word_written = False
        for line, word in list_of_data:
            if line_counter == line:
                new_file.write(word + '\n')
                word_written = True
                break
        if not word_written:
            new_file.write('\n')
        line_counter += 1


# დავალება 3.

# დაწერეთ პითონის პროგრამა, რომელიც წაიკითხავს ორ ფაილს და მათ გაერთიანებულს ჩაწერს
# ახალ ტექსტურ ფაილში. გაერთიანებული ფაილი წაიკითხეთ და დაბეჭდეთ ტერმინალში.

with open('file1.txt', 'w') as file1:
    file1.write('Hello, world!\n')

with open('file2.txt', 'w') as file2:
    file2.write('This is a test.\n')


with open('file1.txt', 'r') as file1:
    read1 = file1.read()


with open('file2.txt', 'r') as file2:
    read2 = file2.read()


with open('combined.txt', 'w') as combined:
    combined.write(read1)
    combined.write(read2)


with open('combined.txt', 'r') as combined:
    content = combined.read()

print(content)

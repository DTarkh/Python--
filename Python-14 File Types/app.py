# დავალება 1.

# გამოიყენეთ  titanic.csv

# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი
# “survived.csv” და ჩაწერეთ მხოლოდ გადარჩენილების ინფორმაცია.

import csv


# with open("titanic.csv", "r") as file:
#     survived_list = []
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         if row['Survived'] == '1':
#             survived_list.append(row)

#     print(survived_list)

# fieldnames = csv_reader.fieldnames

# with open('survived.csv', 'w') as new_file:
#     csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
#     csv_writer.writeheader()
#     csv_writer.writerows(survived_list)


# დავალება 2.

# გამოიყენეთ organizations-100.csv

# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი
# “sorted_csv.csv” და ჩაწერეთ დასორტირებული ინფორმაცია,
# დაასორტირეთ თანამშრომელთა რაოდენობის მიხედვით

# with open('organizations-100.csv', 'r') as organization:
#     reader = csv.DictReader(organization)
#     data = list(reader)

#     sorted_list = sorted(data, key=lambda line: int(
#         line["Number of employees"]))

#     for row in sorted_list:
#         print(row)

# with open("sorted_csv.csv", "w") as sorted_csv:
#     headers = reader.fieldnames
#     write_list = csv.DictWriter(sorted_csv, fieldnames=headers)
#     write_list.writeheader()
#     write_list.writerows(sorted_list)


# დავალება 3.

# გამოიყენეთ organizations-100.csv

# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი
# “ssl_companies.csv” და ჩაწერეთ მხოლოდ აიდი, კომპანიის სახელი,
# ვებ საიტი, ინდუსტრია და დასაქმებულების რაოდენობა ისეთი კომპანიების
# რომელთაც აქვთ ssl-ით დაცული ვებსაიტი(HTTPS)


with open("organizations-100.csv", "r") as file:
    new_list = []
    read_csv = csv.DictReader(file)
    for row in read_csv:
        if 'https' in row["Website"]:
            new_list.append(row)


keys_to_keep = ["Organization Id", "Name",
                "Website", "Industry", "Number of employees"]
filtered_list = []

for item in new_list:
    filtered_dict_line = {key: item.get(key) for key in keys_to_keep}
    filtered_list.append(filtered_dict_line)


for line in filtered_list:
    print(line)


with open("ssl_companies.csv", "w") as company_csv:
    headers = ['Organization Id', 'Name', 'Website',
               'Industry', 'Number of employees']
    write_list = csv.DictWriter(company_csv, fieldnames=headers)
    write_list.writeheader()
    write_list.writerows(filtered_list)

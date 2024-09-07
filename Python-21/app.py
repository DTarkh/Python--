

# წაიკითხეთ მოცემული ფაილი.

import json

with open("movies.json", "r") as movies_json_file:
    movies_deserilized = json.load(movies_json_file)


# ამავე ფაილში ჩაწერეთ ის
# ფილმები, რომელთა გამოშვების თარიღიც არის 2000-ზე მეტი
# და ჟანრი არის Crime,

filtered_list = []

for movie in movies_deserilized:
    for result in movie['results']:

        # print(result['release_date'])
        # print(result['genres'])

        split = result['release_date'].split('-')
        str_to_int = int(split[0])
        # print(str_to_int)

        if str_to_int >= 2000 and 'Crime' in result['genres']:

            # Crime სიტყვა ჟანრში შეცვალეთ New_Crime-ით.
            result['genres'].remove('Crime')
            result['genres'].append('New crime')
            # print(result)
            filtered_list.append(result)


# print(filtered_list)


# გასატეტად ჯერ აქ ჩავწერ რომ დავინახო რა იწერება

dump_json = json.dumps(filtered_list, indent=4)

with open("movies_test.json", "w") as movies_jason_file:
    write_lines = movies_jason_file.write(dump_json)


# with open("movies.json", "a") as movies_jason_file:
#     write_lines = movies_jason_file.write(dump_json)


# ამავე ფაილში ჩაწერეთ ისეთი ფილმები,
# რომელთა გამოშვების თარიღიც არის 2000-ზე ნაკლები,
# ჟანრი არის Drama და ჟანრის სახელი ჩაუწერეთ Old_Drama.


filtered_list_two = []

for movie in movies_deserilized:
    for result in movie['results']:

        split = result['release_date'].split('-')
        str_to_int = int(split[0])
        # print(str_to_int)

        if str_to_int < 2000 and 'Drama' in result['genres']:
            result['genres'].remove('Drama')
            result['genres'].append('Old_Drama')
            filtered_list_two.append(result)


print(filtered_list_two)


dump_json_two = json.dumps(filtered_list_two, indent=4)

with open("movies_test_two.json", "w") as movies_json_file:
    write_lines = movies_json_file.write(dump_json_two)


# with open("movies.json", "a") as movies_json_file:
#     write_lines = movies_json_file.write(dump_json_two)


# იმ ფილმებს, რომელიც 2000 წელს არის გამოშვებული ჟანრში
# ჩაუმატეთ New_Century და ეს ფილმებიც ამავე ფაილში ჩაწერეთ.

filtered_list_three = []

for movie in movies_deserilized:
    for result in movie['results']:

        split = result['release_date'].split('-')
        str_to_int = int(split[0])
        print(str_to_int)

        if str_to_int == 2000:
            result['genres'].append('New century')
            filtered_list_three.append(result)


print(filtered_list_three)


dump_json_three = json.dumps(filtered_list_three, indent=4)

with open("movies_test_three.json", "w") as movies_json_file:
    write_lines = movies_json_file.write(dump_json_three)

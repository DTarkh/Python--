# დავალების შესასრულებლად გამოიყენეთ movies.json

# წაიკითხეთ მოცემული ფაილი.
#
# ამავე ფაილში ჩაწერეთ ის
# ფილმები, რომელთა გამოშვების თარიღიც არის 2000-ზე მეტი
# და ჟანრი არის Crime,
#
# Crime სიტყვა ჟანრში შეცვალეთ New_Crime-ით.
#
# ამავე ფაილში ჩაწერეთ ისეთი ფილმები,
# რომელთა გამოშვების თარიღიც არის 2000-ზე ნაკლები,
# ჟანრი არის Drama და ჟანრის სახელი ჩაუწერეთ Old_Drama.
#
#
# იმ ფილმებს, რომელიც 2000 წელს არის გამოშვებული ჟანრში
# ჩაუმატეთ New_Century და ეს ფილმებიც ამავე ფაილში ჩაწერეთ.

import json

with open("movies.json", "r") as movies_jason_file:
    movies_deserilized = json.load(movies_jason_file)

filtered_list = []

for movie in movies_deserilized:
    for result in movie['results']:
        
        # print(result['release_date'])
        # print(result['genres'])

        split = result['release_date'].split('-')
        str_to_int = int(split[0])
        # print(str_to_int)
   
    
        
        if str_to_int >= 2000 and 'Crime' in result['genres']:
            # print(result)
            filtered_list.append(result)


print(filtered_list)





dump_json = json.dumps(filtered_list, indent=4)

with open("moviess.json", "w") as movies_jason_file:
    write_lines = movies_jason_file.write(dump_json)

        








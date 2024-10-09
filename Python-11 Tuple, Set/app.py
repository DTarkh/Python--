# დავალება 1.

# შექმენით ცვლადი squared_numbers რომელიც შეიცავს 1-დან 10-ის ჩათვლით
# კვადრატში აყვანილ რიცხვებს(არ შეავსოთ ხელით)

# for squared_numbers in range(1, 11):
#     print(squared_numbers ** 2)


# დავალება 2.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს სტრინგს,
# დააბრუნეთ სეტი, რომლის ელემენტებიც არის სტრინგში არსებული თითოეული სიმბოლო


# def create_set(string_value):
#      return set(string_value)

# print(create_set("dato"))

# დავალება 3.

# დაწერეთ ფუნქცია რომელიც ატრიბუტად მიიღებს ორ tuple ტიპის
# მონაცემს, ფუნქციამ უნდა გააერთიანოს ეს ორი tuple და დააბრუნოს ერთი მთლიანი დუბლიკატების გარეშე, შექმენით სია duplicated_values და
# მასში დაამატეთ ის ინფორმაცია მხოლოდ ერთხელ, რომელიც დუბლირებული სახით გვხვდება tuple-ში, დაბეჭდეთ მოცემული სია

# example:
tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)

# output:
# combined_tuple: (1,2,3,4,5,6,7)
# duplicated_values: [4,5,6]


# def combine(first_tuple, second_tuple):

#     duplicated_values = []

#     combined = first_tuple + second_tuple
#     turn_to_tuple = tuple(set(combined))

#     for i in combined:
#         if combined.count(combined[i]) > 1:
#             duplicated_values.append(combined[i])

#     turn_to_set = list(set(duplicated_values))

#     return turn_to_set, turn_to_tuple


# print(combine(tuple1, tuple2))

# დავალება 4.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს ტაპლს, დააბრუნეთ
# ტაპლი სადაც პირველ და ბოლო ელემენტს შეცვლილი ექნება ადგილები:

# input: (1, 2, 3, 4)
# output: (4, 2, 3, 1)

numbers = (1, 2, 3, 4)


# def change_order(tuple_value):
#     if len(tuple_value) < 2:
#         return tuple_value
#     return (tuple_value[-1], ) + tuple_value[1:-1] + (tuple_value[0], )


# print(change_order(numbers))

# დავალება 5.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს ერთმანეთში ჩადგმულ
#  ტაპლს, დააბრუნეთ ერთი სრული ტაპლი, სადაც მოცემული იქნება ყველა ელემენტი.

# Input: (1, (2, 3), (4, (5, 6)))
# output: (1, 2, 3, 4, 5, 6)

# num = (1, (2, 3), (4, (5, 6)))
# def flatten_tuple(tuple_value):
#     return (tuple_value[0], ) + tuple_value[1] + ((tuple_value[2][0], ) + tuple_value[2][1])

# print(flatten_tuple(num))
# დავალება 6.

# დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს ორ სეტს, დააბრუნეთ
# სეტი, რომელიც შედგება ტაპლებისგან და ისინი შეიცავენ ორი სეტის ყველა შესატყვისს:

# input: {1, 2}{‘a’, ‘b’}
# output: {(1, ‘a’), (1, ‘b’), (2, ‘a’), (2, ‘b’)}


def merge_sets(set1, set2):
    return {(a, b) for a in set1 for b in set2}


print(merge_sets({1, 2}, {'a', 'b'}))

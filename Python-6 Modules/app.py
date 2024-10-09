# დავალება 1.
# დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრინგს და
# შეამოწმებს არის თუ არა სტრიქონი ანაგრამი. ( ანაგრამი არის სიტყვა
# ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების
# ასოების გადაადგილებით)


# def anagram(string1, string2):
#     first_string = sorted(string1)
#     second_string = sorted(string2)
#     if first_string == second_string:
#         return f"string {string1} and {string2} are anagrams"
#     else:
#         return f"string {string1} and {string2} are not anagrams"


# print(anagram("dato", "otad"))

# დავალება 2.
# დაწერეთ პითონის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს
# სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში
# რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს
# მისი რაოდენობა


# def check_char_repetition (string, char):
#     number_of_chars = string.count(char)
#     return f"the letter {char} is repeated {number_of_chars} times"

# print(check_char_repetition("homeland", "a"))


# დავალება 3.
# დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და
# გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.


def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


print(fibonacci(6))

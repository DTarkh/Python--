# საშინაო დავალება - შექმენით სტუდენტის ობიექტი
# სახელი, გვარი, დაბადების წელი და ქულა.
# შექმენით ამ კლასის სამი სხვადასხვა ობიექტი.
# დაწერეთ ფუნქცია რომელიც არგუმენტად მიიღებს ობიექტს.
# ჯერ სცდის JSON-თ ჩაწერას თუ პროცესი წარუმატებელი აღმოჩნდა,
# სცდის pickle-ით ჩაწერას, თუ ფიქლიც წარუმატებელი აღმოჩნდა
# შემდეგ სცდის Dill-ით ჩაწერას. თუ ვერცერთით ვერ ხდება
# ჩაწერა დააბრუნოს პასუხი რომ ვერცერთ მეთოდი ვერ
# ასერიალიზებს გადაცემულ ობიექტს



class Student:
    def __init__(self, name, surname, birth_year, grade):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.grade = grade

    

student1 = Student("David", "Tarkhnishvili", 1992, 100)
student2 = Student("Mary", "Popins", 1986, 87)
student3 = Student("Elizabeth", "Queen", 1996, 93)


import json
import pickle
import dill


def serialize_data(obj):
    try:
        with open("file.json", "w") as f:
            json.dump(obj, f)
        print("successfully serialized")
    except (TypeError, json.JSONDecodeError )as error:
        print(f"JSON serialization failed: {error}")
        try:
            with open("file.pkl", "wb") as f:
                pickle.dump(obj, f)
            print("Successfully serialized with Pickle.")
        except pickle.PicklingError as error:
            print(f"Pickle serialization failed: {error}")
            try:
                with open("file.dill", "wb") as f:
                    dill.dump(obj, f)
                print("Successfully serialized with Dill.")
            except dill.PicklingError as error:
                print(f"Dill serialization failed: {error}")
                print("Unable to serialize the object with any method")

print(serialize_data(student1))
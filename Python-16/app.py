# დავალება 1.

# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. შექმენით კლასი
# სახელწოდებით BankAccount, ისეთი ატრიბუტებით, როგორიცაა account_number,
# account_holder და balance. აღწერეთ ფულის ჩარიცხვის და გამოტანის მეთოდები.
#  შექმენით რამდენიმე ობიექტი და განახორციელეთ რამდენიმე ტრანზაქცია.


class BankAccount:
    account_number = "TB3444A422B00006"
    account_holder = "John Doe"
    balance = 576

    def add_money(self, money):
        self.balance += money
        return self.balance

    def get_money(self, money):
        self.balance -= money
        return self.balance


add = BankAccount()
print(add.add_money(200))

get = BankAccount()
print(get.get_money(500))

# დავალება 2.

# შექმენით კლასი სახელწოდებით Student ატრიბუტებით, როგორიცაა name,
# student_id და courses(კურსების სია, რომელშიც სტუდენტი არის ჩარიცხული).
# აღწერეთ სტუდენტის ინფორმაციის და კურსების ჩვენების მეთოდები. შექმენით
# რამდენიმე ობიექტი და დაარეგისტრირეთ სხვადასხვა კურსებზე.


class Student:


    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = courses
    

    def get_info(self):
        print( f"Name: {self.name}, Student ID: {self.student_id}, Courses: {self.courses}")

    def register_on_math(self):
        print("You have successfully registered on Math course")

    def register_on_English(self):
        print("You have successfully registered on English course")


student1 = Student("David", "334AA", "Math")
student2 = Student("Diliya", "556BB", "How to get Rich")
student1.get_info()
student2.get_info()
student1.register_on_math()

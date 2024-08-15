# დავალება 1.

# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. შექმენით კლასი
# სახელწოდებით BankAccount, ისეთი ატრიბუტებით, როგორიცაა account_number,
# account_holder და balance. აღწერეთ ფულის ჩარიცხვის და გამოტანის მეთოდები.
#  შექმენით რამდენიმე ობიექტი და განახორციელეთ რამდენიმე ტრანზაქცია.


class BankAccount:

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def add_money(self, money):
        self.balance += money
        return self.balance

    def get_money(self, money):
        self.balance -= money
        return self.balance


client = BankAccount("TB3444A422B00006", "John Doe", 576)
client2 = BankAccount("TB3444A422B00006", "David Tarkhnishvili", 1420)

print(f"{client.account_holder} has {client.balance} GEL on balance")
print(f"He is adding 200 that results to have {client.add_money(200)}")
print(f"He is withdrawing 300 that results to have {client.get_money(300)}")
print(f"{client2.account_holder} has {client2.balance} GEL on balance")
print(f"He is withdrawing 550 that results to have {client2.get_money(500)}")

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
        print(f"Name: {self.name}, Student ID: {self.student_id}, Courses: {self.courses}")

    def register_on_math(self):
        print("You have successfully registered on \"Math\" course")

    def register_on_English(self):
        print("You have successfully registered on \"English\" course")

    def register_on_HowtogetRich(self):
        print("You have successfully registered on \"How to get Rich course\"")


student1 = Student("David", "334AA", ["Math", "English"])
student2 = Student("Diliya", "556BB", ["How to get Rich", "French", "English"])
student1.get_info()
student2.get_info()
student1.register_on_math()
student2.register_on_HowtogetRich()
student1.register_on_English()

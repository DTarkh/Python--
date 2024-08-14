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

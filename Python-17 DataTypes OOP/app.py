
# აღწერეთ ორი კლასი შემდეგი მონაცემების მიხედვით:

# Person:
# name
# deposit (default value = 1000, მიუთითებს ამჟამად რამდენი აქვს დეპოზიტზე)
# loan (default value = 0, მიუთითებს ამჟამად რამდენი აქვს სესხი აღებული)


# House:
# ID – ბინის საკატასტრო კოდი
# price – ბინის ფასი
# owner – სახლის მეპატრონე (Person ტიპის ობიექტი)
# status – ახალი ბინის დამატებისას სტატუსი არის ყოველთვის “გასაყიდი”


# გაითვალისწინეთ owner-ის მნიშვნელობა არის Person კლასის ობიექტი

# Person კლასში დაამატეთ __str__ მეთოდი რომელიც დააბრუნებს პიროვნების სრულ ინფორმაციას


# შექმენით ორი Person კლასის ობიექტი(მაგალითად ერთი მეპატრონე, მეორე მყიდველი). ასევე
# შექმენით House კლასის ობიექტი რომლის owner იქნება ერთ-ერთი Person ობიექტი

# House კლასში დაამატეთ ბინის გაყიდვის მეთოდი, რომლის დროსაც პარამეტრებად გადაეცემა
# მყიდველი, თუ მეტი პარამეტრი არ გადაეცემა, ამ დროს უნდა შესრულდეს ბინის გაყიდვის
# ოპერაცია(გამყიდველის deposit უნდა გაიზარდოს ბინის ღირებულებით, უნდა შეიცვალოს
# owner და status უნდა გახდეს “გაყიდული”, დაბეჭდეთ შესაბამისი ტექსტი).
#
# თუ ამ მეთოდის
# გამოძახების დროს მყიდველის გარდა პარამეტრად გადაეცა კიდევ ერთი რიცხვი, მაშინ შესრულდეს
#  ბინის სესხით გაყიდვის ოპერაცია, სადაც პარამეტრად გადაცემული რიცხვი მიუთითებს მყიდველის
# მიერ აღებული სესხის რაოდენობას, მეთოდმა კი უნდა შეასრულოს შემდეგი ოპერაციები: გამყიდველის
# deposit უნდა გაიზარდოს ბინის ღირებულებით, owner უნდა შეიცვალოს, status გახდეს “გაყიდული სესხით”,
#  მყიდველის სესხი (loan) უნდა გაიზარდოს შესაბამისი რაოდენობით და დაიბეჭდოს გაყიდვის შესაბამისი შეტყობინება.

# კლასის გარეთ მოახდინეთ აღწერილი ფუნქციების გამოძახება


class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f'Person: {self.name}, deposit: {self.deposit}, loan: {self.loan}'


buyer = Person("David", 60000)
seller = Person("Tom")


class House():
    def __init__(self, ID, price, owner, status):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def __str__(self):
        return f'ID: {self.ID}, Price: {self.price}, owner: {self.owner}, status: {self.status}'

    def sell_house(self, buyer, seller, loan=0):
        if loan == 0:
            self.loan = loan
            seller.deposit += self.price
            buyer.deposit -= self.price
            self.owner = buyer
            self.status = "Sold"
            print(f'Seller\'s deposit value is: {seller.deposit}, new owner is: {buyer.name} and status of the house is: \"{self.status}\"')

        else:
            buyer.loan = loan
            self.status = "Sold by loan"
            print(f'Seller\'s deposit value is: {seller.deposit}, new owner is: {buyer.name}, he\'s loan is: {buyer.loan} and status of the house is: \"{self.status}\"')


my_house = House(24242, 50000, seller, "avialable")
print(my_house)

new_owner = my_house.sell_house(buyer, seller)
print(new_owner)

new_owner_by_loan = my_house.sell_house(buyer, seller, 10000)
print(new_owner)

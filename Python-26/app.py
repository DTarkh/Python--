# დაწერეთ პროგრამა ონლაინ ბილეთების გაყიდვის ვებ გვერდისთვის.
# შექმენით მომხმარებლების სია (10-15 პერსონა) უნდა მოახდინოთ
# რიგის მენეჯმენტი ვებსაიტზე, ერთდროულად 5 ადამიანს უნდა შეეძლოს
# ყიდვის სესიაში შესვლა(Semaphore) დაბეჭდეთ რომ მომხმარებელი ცდილობს
# სესიაში შესვლას და თუ შევიდა სესიაში დაბეჭდეთ რომ დაიკავა ადგილი
# კონკრეტულმა მომხმარებელმა. მომხმარებელი რომელიც შესულია სესიაში
# ბილეთს იყიდის 5 წამში (sleep) და გაათავისუფლებს ადგილს შემდეგი
# მომხმარებლისთვის. პროგრამა დაასრულებს მუშაობას როდესაც ყველა
# მომხმარებელი იყიდის ბილეთს.
# პ.ს. გამოიყენეთ parking-ის ნაწილი რომელიც ლექციაზე გავაკეთეთ


import threading
import time




semaphore = threading.Semaphore(5)


def tickets_sell(customer):
    print(f"customer: {customer} has started a session to buy a ticket")
    print(f"customer: {customer} is in the session")
    semaphore.acquire()
    print(f"customer: {customer} has bought a ticket and left")

    time.sleep(5)
    semaphore.release()
list_of_customers = ["customer1", "customer2", "customer3", "customer4", "customer5", "customer6", "customer7", "customer8", "customer9", "customer10"]
threads_list = [threading.Thread(target=tickets_sell, args=(customer,)) for customer in list_of_customers]


for thread in threads_list:
    thread.start()

for thread in threads_list:
    thread.join()



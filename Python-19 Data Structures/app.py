# დავალება 1.

# ლექციაზე განხილულ კოდებს, დააწერეთ კომენტარები თუ რა დროს რა ხდება

# კვანძი რომელსაც გადაეცემა ატრიბუტებად "data" და "next".
class Node:
    def __init__(self, data=None):
        self.data = data
        # None რადგან შეიძლება იყოს 1 ელემენტიანი ლინკდლისტი
        # და ნექსთი არ ექნება.
        self.next = None


class LinkedList:
    def __init__(self):
        # პირველი ელემენტი ვეძახით ჰედს. ის შეიძლება არ გვქონდეს და იყოს ცარიელი
        # ლინკდ ლისტი. ამიტომ დეფაულტ მნიშვნელობას ვუწერთ ნანს.
        self.head = None

    # შევქმენით მეთოდი ახალი ინფორმაციის დასამატებლად.
    # ის ინფორმაციას ამატებს ბოლოდან.
    def append(self, data):
        # იმისთვის რომ ლინკდლისტში შევინახოთ ინფო, მას ის უნდა გადავცეთ ნოუდის
        # სახით. ამიტომ პირველ რიგში ვიყენებთ ჩვენ კლასს და ვქმნით ნოუდ ობიექტს.
        new_node = Node(data)

        # ახლა ვეძებთ ადგილს სად ჩავსვათ ახალი ნოუდი.

        # ვამოწმებთ საერთოდ არის თუ არა რაიმე ინფორმაცია.
        # თუ ჰეადი არის ნანი ანუ არ არსებობს. ნიშნავს რომ ამ ადგილზე
        # უნდა ჩაისვას ნოუდი.
        if self.head is None:
            self.head = new_node
            return

        # ვუშვებთ რომ ბოლო ელემენტი შეიძლება იყოს პირველი ანუ ჰედი.
        last_node = self.head

        # ვაილ ციკლი იმუშავებს იქადე. სანამ last_node ექნება ნექსთი.
        # თუ ნექსთი არის ნანი, ეს ნიშნავს რომ მივედით ბოლო ელემენტზე
        while last_node.next:
            # ბოლო ელემენტი უტოლდება ბოლო ნაპოვნ ელემენტს რომლის
            # ნექსთი ნანია.
            last_node = last_node.next

        # ბოლო ელემენტში ჩავწეროთ ახალი ნოუდი.
        last_node.next = new_node

    def remove_at(self, index):
        # ვამოწმებთ: თუ ინდექს 0 ლე ნაკლებია მაშინ ან სელფ ჰედი ნანია ესეიგი
        # ცარიელია და არაფერია წასაშლელი
        if index < 0 or self.head is None:
            return
        # თუ გადმოვქცეს ინდექსი 0 წასაშლელად მაშინ პირველი ელემენტი ინდექსად 0
        # სელფ ჰედის ადგილი უნდა დაიკავოს მის შემდეგ მდგომმა ელემენტმა
        if index == 0:
            self.head = self.head.next
            return
        # ვეძებთ ელემენტს რომელიც უნდა წაიშალოს, ჩავთვალოთ რომ პირველი ელემენტი
        current_node = self.head
        # აგრეთვე ვნახოთ რა ინდექსზე დგას ელ ელემენტი
        current_position = 0

        # ვაილ ციკლი დაასელექტებს რისი წაშლაც გვინდა იმაზე 1 ით ნაკლლებ ინდექსზე მდგომს
        while current_node.next and current_position < index - 1:
            # თაავის ადგილზე სვამს მის შემდეგ მდგომ ელემენტს
            current_node = current_node.next
            # რომელ ინდქსზე დგას ამის დასათვლელად, ყველი გადაადგილების დროს
            # ინდექსი იზრდება შესაბამისად 1 ით.
            current_position += 1

        # ასელექტებს ბოლო ელენენტს რომელიც უნდა წაიშალოს და ის ამოვარდება ლისტიდან
        # რადგან მას ვუტოლებთ იმ ელემენტს რომელიც უკვე აღარ არსებობს ლისტში. ნექსთის ნექსთი ელემენტი.
        if current_node.next:
            current_node.next = current_node.next.next

    def display(self):
        # ჩავთვალოთ რომ ის ნოუდი რომლის დაბჭდვა გვინდა არის ჰედი ანუ პირველი
        # და მხოლოდ ერთი რომელიც არის ლინკდლისტში.
        current_node = self.head

        # ციკლო იმუშავებს თუ ნოუდი არ იქნება ნანი
        while current_node is not None:
            # ნოუდს ვბეჭდავთ
            print(current_node.data, end=" -> ")
            # დაბეჭვდის შემდეგ ნოუდის მნიშვნელობა ხდება მის შემდეგ არსებული ნოუდი
            # და ის იბეჭდება.
            current_node = current_node.next


linked_list = LinkedList()
linked_list.append("Hello")
linked_list.append(10)
linked_list.append(True)
linked_list.append(5.5)
linked_list.display()
print()
linked_list.remove_at(2)
linked_list.remove_at(0)
linked_list.display()


# იქმნება ნოუდი ისევე როგორც დაკავშირებული სიების შემთვევაში რომლიც შეიცავს რაღაც დატას.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # აქ პირველ ელემენტს ქვია ტოპ ნოუდი.დასაწსისთვის არის ნანი.
        self.top_node = None
        # დაითვლის მის სიგრძეს, დასაწსისთვის უდრის 0-ს
        self.length = 0

        # მეოთოდი რომელიც ამოწმებს მასში არის დატა თუ არა.
        # აბრუნებს თრუ ან ფოლს.

    def empty(self):
        return self.length == 0

    # აბრუნებს სტეკის სიგრძეს
    def size(self):
        return self.length

    def push(self, data):
        # შევქმმენიტ ახალი ნოუდი.
        new_node = Node(data)
        # new_node უნდა გახდეს self.top_node. უკვე არსებული ნოუდი რომ ად დავკარგოთ ამიტომ
        # new_node ის შემდეგს ვსვავთ ტოპ ნოუდად
        new_node.next = self.top_node
        # new_node ის შემდეგი გახდება ტოპი
        self.top_node = new_node
        # როდესაც ვამატებთ ელემენტს სიგრძე იზრდება, ამიტომ ვზრდით სიგრძეს 1 ით
        self.length += 1

    # პოპის მსგავსია, მაგრამ ის არ შლის ელემენტს. მხოლოდ კითხულობს

    def top(self):
        if not self.empty():
            return self.top_node.data
        else:
            raise IndexError("Stack Is Empty")

    def pop(self):
        # ვამოწმებთ არის თუ არა ცარიელი
        if not self.empty():
            # popped_item  არის ცვლადი რომელშიც ინახება ოს რაც უნდა ცავშალოთ და დავინახოთ  self.top_node.data არის ბოლო ელემენტი
            popped_item = self.top_node.data
            # ბოლო ელემენტს ამოაგდებს ლისტიდან და მის ადგილს დაიკავებს მისი ნექსთი ანუ ბოლოს წინა ელემენტი
            self.top_node = self.top_node.next
            # ვამცირებთ სიგრძეს შესაბამისად როდესაც ამვოარდა ელემენტი.
            self.length -= 1
            return popped_item
        else:
            # თუ ცარიელია დააბრუნებს რომ ცარიელია.
            raise IndexError("Stack Is Empty")


stack = Stack()

print(f"Stack Is Empty: {stack.empty()}")
print(f"Stack Size: {stack.size()}")

stack.push(10)
stack.push(5)
stack.push(20)
stack.push(50)

print(f"Stack Is Empty: {stack.empty()}")
print(f"Stack Size: {stack.size()}")

print(stack.pop())
print(f"Stack Size: {stack.size()}")
print(stack.pop())
print(f"Stack Size: {stack.size()}")
print(stack.pop())
print(f"Stack Size: {stack.size()}")
print(stack.pop())
print(f"Stack Size: {stack.size()}")

print(stack.top())


# დავალება 2.

# დაწერეთ value გადაწოდების შედეგად ამოშლის ლოგიკა დაკავშირებულ სიებში

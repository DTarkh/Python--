
# დავალება 1.

# დაწერეთ ფუნქცია, რომელიც უბრალოდ აბრუნებს არგუმენტად გადაწოდებულ რიცხვს,
#  დაუწერეთ დეკორატორი, რომელიც შეამოწმებს, რომ რიცხვი უნდა იყოს დადებითი,
#  თუ არის უარყოფითი ამ შემთხვევაში დააბრუნეთ ValueError შესაბამისი ტექსტით,
# სხვა შემთხვევაში აამოქმედეთ ფუნქცია, შედეგი კი დაბეჭდეთ დეკორატორიდან.


import time


def decorator_function(func):
    def wrapper(*args, **kwargs):
        x = args[0]
        if x > 0:
            return func(x)
        else:
            return "\'value error\': The number is below zero."

    return wrapper


@decorator_function
def return_number(number):
    return number


print(return_number(2))


# დავალება 2.

# დაწერეთ პირველი დავალება ფუნქტორის გამოყენებით


class Functor:
    def __call__(self, number):
        if number > 0:
            return number
        else:
            return "\'value error\': The number is below zero."


new_functor = Functor()
print(new_functor(2))

# დავალება 3.

# დაწერეთ დეკორატორი, რომელიც გამოთვლის ფუნქციის მოქმედების დროს და დაბეჭდავს
#  ტერმინალში. დროის აღსაქმელად გამოიყენეთ time.time()


def time_length(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper


@time_length
def return_number(number):
    return number


print(return_number(2))


# დავალება 4.

# შექმენით მეტაკლასი LoggingMeta, რომელიც ყოველი კლასის შექმნის დროს
# დაბეჭდავს თუ რა სახელის მქონე კლასი იქმნება.


def init(self, name, age):
    self.name = name
    self.age = age


def class_name(self):
    return self.__class__.__name__


LoggingMeta = type('person', (object, ), {
    '__init__': init,
    'class_name': class_name,
})


new = LoggingMeta('Dato', 31)
print(new.__class__.__name__)

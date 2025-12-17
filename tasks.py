# 1 задача
from functools import wraps

a = int(input())

if a > 0:
    print("А положительное")
elif a < 0:
    print("А отрицательное")
else:
    print("A равно 0")


# 2 задача
b = input()

if b.endswith("test"):
    print("Yes")
else:
    print("No")

# 3 task

c = int(input("Введите возраст "))

if c >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")


# 4 task

d = input("Введите строку: ")

if d == "":
    print("Строка пустая!")
else:
    print("Строка не пустая")

# 5 task

passw = "qwert12345"
up = input("Введите пароль: ")

if up == passw:
    print("Пароль верный!")
else:
    print("Ошибка!")

# 6 task

e = input("Введите строку: ")

if "error" in e:
    print("Ошибка найдена")
else:
    print("Ошибки нет")

# 7 task

f = int(input("Введите число: "))

if f % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")

# 8 task

j = input("Введите строку: ")

if j[0].isupper():
    print("Верно")
else:
    print("Неверно")

# 9 task

h = input("Введите строку: ")

if len(h) > 10:
    print("Строка длинная")
else:
    print("Строка короткая")

# 10 task

i = input("Введите символ: ")

if i in "aeiou":
    print("Это гласная")
else:
    print("Это не гласная")

# 11 task

name = input("Введите имя: ")

if name == "Иван":
    print("Привет, студент")
else:
    print("Имя другое")

# 12 task

s_1 = input("Введите имя: ")
s_2 = input("Введите фамилию: ")

if s_1 == s_2:
    print("Строки равны")
else:
    print("Строки НЕ равны")

# 13 task

num = int(input("Введите число: "))

if 1 <= num <= 100:
    print("Число в диапазоне")
else:
    print("Число вне диапазона")

# 14 task

ss = input("Введите строку: ")

if ss.isdigit():
    print("Строка состоит только из цифр")
else:
    print("Строка содержит другие символы")

# 15 task

kk =  input("Введите строку: ")

if kk.endswith("a"):
    print("Строка заканчивается на 'a'")
else:
    print("Не заканчивается на 'a'")

# hw 1 task

s = "test123"

a = input("Input: ")

a = input("Input: ")
gl = "aeuioy"
count = 0

for i in a:
    if i in gl:
        count += 1
print("Количество гласных: ", count)


def print_message():
    print("Hello, world!")

print_message()

# functions

# 1
def add(a, b):
    c = a + b
    print(c)
add(7, 7)

# 2
def calculate_area(lenght, width):
    print("square: ", lenght + width)

calculate_area(3, 7)

# 3
def calculate_area(lenght, width):
    print("square: ", lenght + width)

calculate_area(3, 7)

# 4
def display_info(name, age):
    print(f'Name: {name}, Age: {age}')

display_info("Alex", 7)

display_info(55, "Sam")

# 5

def display_info(name, age):
    print(f'Name: {name}, Age: {age}')

display_info("Alex", 7)

display_info(55, "Sam")

# 6
def configure_settings(volume = 50, brightness = 70):
    print(f'volume: {volume}, brightness: {brightness}')


configure_settings(60, "dark")

configure_settings()

# 7
def print_all(*args):
    for arg in args:
        print(arg)

print_all(1, 3, 5, 33, 3, 3, 5, 'asd')

# 8 return
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# 9
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(3))
a = is_even(2)
b = is_even(7)
print(a, b)

# 10 lambda

mult = lambda x: x*2

print(mult(3))

# 11

words = ['apple', 'banana', 'orange', 'fff']
words.sort(key=lambda word: len(word))

print(words)

# 12
def plus():
    pass
def minus():
    pass

# 13 lambda
test_results = [
    {"name": "login_test", "status": "passed", "duration": 2.1},
    {"name": "payment_test", "status": "failed", "duration": 3.5},
    {"name": "logout_test", "status": "passed", "duration": 1.2}
]
passed_tests = filter(lambda test: test["status"] == "passed", test_results)
passed_names = [test["name"] for test in passed_tests]

print("Успешные тесты:", passed_names)

# 14 lambda

def apply_test_check(check_func, test_results):
    passed_iter = filter(check_func, test_results)
    passed_count = len(passed_list)
    return passed_count

test_results = [
    {"status": "passed"}, {"status": "failed"}, {"status": "passed"}
]
check_lambda = lambda r: r.get("status") == "passed"
result = apply_test_check(check_lambda, test_results)

print(f"Прошло тестов: {result}")

# 15 lambda

def filter_logs(logs, filter_func):
    return [log for log in logs if filter_func(log)]

logs = [
    {"level": "INFO", "message": "Test started"},
    {"level": "ERROR", "message": "Login failed"},
    {"level": "WARNING", "message": "Timeout occurred"}
]

error_logs = filter_logs(logs, lambda log: log.get("level") == "ERROR")
print("Ошибки:", error_logs)

# 16 lambda

def generate_report(title, *test_names, format="html", **options):
    print(f"Отчет: {title}")
    print(f"Формат: {format}")

    if test_names:
        print("Тесты:", ", ".join(test_names))

    for key, value in options.items():
        print(f"{key}: {value}")

generate_report("Daily Report", "test1", "test2", "test3", format="pdf", author="Tester")

# 17 циклы (hw 6, task 3)

u = input('input: ')
a = u.split()
for i in a:
    print("Test Case:", i)

# 18 циклы (hw 6, task 4)
pd = ""

while pd != "admin":
    pd = input('Введите парооль:')
    if pd == "admin":
        print("Верный пароль!")
        break

# 19 циклы (hw 6, task 5)
for i in range(1, 11,):
    if i % 3 == 0:
        continue
    print(i)

# 19 Декораторы

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Launch the function {func.__name__} with arguments {args}, {kwargs}.")
        func(*args, **kwargs)
    return wrapper
@logger
def print_dog_namen(**kwargs):
    """Function just printin dogs names"""
    for key, item in kwargs.items():
        print(item)


#19.1
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Launch the function {func.__name__} with arguments {args}, {kwargs}.")
        func(*args, **kwargs)
    return wrapper

@logger
def print_dog_namen(**kwargs):
    """Function just printin dogs names"""
    for key, item in kwargs.items():
        print(item)

print(print_dog_namen.__doc__)
print(print_dog_namen.__name__)
#20 l

def say_hello(func):
    print("Начинается тест")
    return func

@say_hello
def test():
    print("Тест запущен")

print(test())


# 21 Decotator
def say_hello(func):
    def wrapper():
        print("Test starts")
        func()
    return wrapper

@say_hello
def ttest():
    print("Tests launched")

ttest()

# 22

sp = input("input: ").split()
new = []

for i in sp:
    i = int(i)
    if i % 5 == 0:
        new.append(i)

print(new)

# 23

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))

# 24 замыкание

def make_multip(factior):
    c = 5
    def mult(x):
        return x * factior - c
    return mult

three = make_multip(3)

print(three(4))

# 25 decorator

def decor(func):
    def wrapper(firstname, lastname):
        print(f"Get {firstname} and {lastname}.")
        func(firstname, lastname)
    return wrapper

@decor
def print_name(fname, lname):
    print(f"Name: {fname}, Lastname: {lname}")

print_name("Alex", "Test")

# 26
def decor(func):
    def wrapper(*args, **kwargs):
        print(f"Get {args} and {kwargs}.")
        func(args[0], args[1])
    return wrapper

@decor
def print_name(fname, lname):
    print(f"Name: {fname}, Lastname: {lname}")

print_name(33, "Alex", "Test", 33,  dog = "Bom")

# 27 decorator + parameters

def decorator_wrapper(arg1, arg2):
    def real_decoratir(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return real_decoratir

@decorator_wrapper(1, 2)
def func(*args):
    for arg in args:
        print(arg)


func(1, 2, 78)

#28 Class

class Dog:
    """Class for Dogs"""
    pass

jack = Dog()
sky = Dog()

#print(type(jack)) #<class '__main__.Dog'>
#print(isinstance(sky, Dog)) #True
#print(sky.__doc__) #Class for Dogs
print(jack) #<__main__.Dog object at 0x10272e150>

#29 class

class Dog:
    """Class for Dogs"""
    cls_name = 'Dog'
    def __init__(self):
        self.name = "NoName"
        self.nose_temp = 24

sky = Dog()
jack = Dog()
jack.name = "jack"
jack.nose_temp = 24

print(sky.name, jack.name, jack.cls_name)

# 1 task
class Car:
    def drive(self):
        pass

# 2 task
class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


s1 = Student("Svetlana", "Ples")

print(s1.fname, s1.lname)

# 3 task
class Rectangle:
    pass

# 4 task
class Book:
    def read(self):
        print("Книга")

b = Book()
b.read()

# 5 task

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))

# task 1.1
class Car:
    def __init__(self, speed):
        self.speed = speed

    def drive(self):
        pass

car1 = Car(120)
print(car1.speed)

#task 1.2
class Student:
    total_students = 0

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        Student.total_students += 1


s1 = Student("Max", "Test")
s2 = Student("Bob", "Smith")

print(s1.fname, s1.lname)
print("Количество студентов:", Student.total_students)

#task 2.1
class Car:
    def __init__(self, speed):
        self.speed = speed   # Атрибут экземпляра

    def drive(self):
        print(f"Машина едет со скоростью {self.speed} км/ч")

    def accelerate(self, amount):
        """Увеличивает скорость на значение amount"""
        self.speed += amount
        print(f"Скорость увеличена! Текущая скорость: {self.speed} км/ч")


car1 = Car(120)
print(car1.speed)

car1.drive()
car1.accelerate(20)
car1.drive()

# наследоование
class Animal:
    def speak(self):
        print("Animal can speak")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

cat = Cat()
cat.speak()   # Meow

dog = Dog()
dog.speak()

# инкапсуляция

class User():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def full_name(self):
        return f"{self.fname} {self.lname}"


user = User("Ivan", "Petrov")
print(user.fname)

user.fname = "Test"

#   @setter

class User():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lnamepü

    @property
    def full_name(self):
        return f"{self.fname} {self.lname}"

    @full_name.setter
    def full_name(self, new_full_name):
        l = new_full_name.split(" ")
        self._fname = l[0]
        self._lname = l[1]


user = User("Ivan", "Petrov")
print(user.full_name)

user.full_name = "Test TEst"
print(user.full_name)

#abstraction


from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def read(self):
        pass

class File(DataSource):
    def __init__(self, content: str):
        self.content = content

    def read(self):
        return self.content.splitlines()

class DB(DataSource):
    def read(self):
         return[{"id": 1, "name": "test"}]

def load_data(ds: DataSource):
    data = ds.read()
    print("Loaded data:", data)

load_data(File("line\nline2"))
load_data(DB())


# abstractions
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speech(self):
        pass

class Dog(Animal):
    def speech(self):
         return "Woof, woof"

class Cat(Animal):
    def speech(self):
         return "Meow"

class Horse(Animal):
    def speech(self):
        return "EEgogo"


def say_something(ds: Animal):
    data = ds.speech()
    print("This animal says:", data)

say_something(Dog())
say_something(Cat())

# task 1

def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        print("Индекс вне диапазона")
        return None
    except TypeError:
        print("Некорректный тип индекса")
        return None

data = [10, 20, 30]

print(get_item(data, 1))     # 20
print(get_item(data, 5))     # сообщение, None
print(get_item(data, "1"))   # сообщение, None

# task 2
class User:
    def __init__(self, username, is_active=True, role="user"):
        self.username = username
        self.is_active = is_active
        self.role = role

    def __str__(self):
        return f"User(username='{self.username}', is_active={self.is_active}, role='{self.role}')"


u1 = User("alice")
u2 = User("bob", is_active=False)
u3 = User("admin", role="admin")

print(u1)
print(u2)
print(u3)

# task __new__, __init__

class User:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    def __init__(self, name):
        self.name = name


u = User("Alex")


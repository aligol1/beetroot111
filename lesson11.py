"""
'''LEsson 11 Task 1 School
Make a class structure in python representing people at school.
Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods and
attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example,
the name should be a Person attribute, while salary should only be available to the teacher. '''


class Person:
    count_person = 0
    def __init__(self, name, lastname, gender, birthday):
        self.name = name
        self.lastname = lastname
        self.gender = gender
        self.birthday = birthday

class Student(Person):
    count_student = 0

    def __init__(self, name, lastname, gender, birthday, group):
        super(Student, self).__init__(name, lastname, gender, birthday)
        self.group = group
        Student.count_student += 1

class Teacher(Person):
    count_teacher = 0

    def __init__(self, name, lastname, gender, birthday, subject, salary):
        super(Teacher, self).__init__(name, lastname, gender, birthday)
        self.subject = subject
        self.salary = salary
        Teacher.count_teacher += 1

    def add_salary(self, percent):
        self.salary = self.salary * percent
        print(self.salary)

    def change_subject(self, newsubj):
        self.subject = newsubj




if __name__ == '__main__':
    student1 = Student('Игопь', 'Алергуш', 'м', '20011214', '1st')
    student1 = Student('Олег', 'Грозный', 'м', '20011214', '2nd')
    teacher1 = Teacher('Юрий', 'Иванов', 'м', '19981214', 'Physics', 1200)
    teacher2 = Teacher('Игопь', 'Алергуш', 'м', '19901214', 'Chemistry',1300)
    teacher3 = Teacher('олег', 'федоров', 'м', '19981214', 'Math', 1200)
    teacher4 = Teacher('Игнат', 'петров', 'м', '19901214', 'Algebra',1500)

    print(Teacher.count_teacher)
    print(teacher4.name)
    print(student1.birthday)
    print(teacher4.salary)
    print(Person.count_person)
    Teacher.add_salary(teacher3,1.1)
    Teacher.change_subject(teacher1, "music")
    print(teacher1.subject)

'''Task 2

Mathematician
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
```
class Mathematician:
    pass
m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
```
'''

class Mathematician:
    def __init__(self, list_of_integers):
        self.list_of_integers = list_of_integers

    def square_nums(self):
        return [i**2 for i in self.list_of_integers]

    def remove_positives(self):
        return [i for i in self.list_of_integers if 1 > 0]

    def filter_leaps(self):
        return [i for i in self.list_of_integers if i > 0 and i % 4 == 0]


if __name__ == "__main__":
    m1 = Mathematician([1, 49, 123, 34535, 4, -1])
    m2 = Mathematician([-10, -2, 0, -90, 200, 13])
    m3 = Mathematician([2001, 2005, 2004, 2008, 2020, 2022])
    print(m1.square_nums())
    print(m2.remove_positives())
    print(m3.filter_leaps())
"""

'''Lesson 11 Task 3 Product Store
Write a class Product that has three attributes:
type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement
additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
```

class Product:
    pass
class ProductStore:
pass
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product(Food, 'Ramen, 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell(‘Ramen’, 10)
assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
```
'''


class Product:
    def __init__(self, group, name, price):
        self.group = group
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.price_premium = 1.3
        self.stock = []
        self.income = 0

    def add(self, product, amount):
        self.stock.append([product.group, product.name, product.price*self.price_premium, amount])

    def set_discount(self, product_name, discount_percent):
        for i in self.stock:
            if i[2] == product_name:
                i[3] * discount_percent
            else:
                print('ne to')

    def sell_product(self, product_name, amount):
        for i in self.stock:
            if i[2] == product_name and i[4] > amount:
                i[4] -= amount
            else:
                print("Недостаточно товара")

    def get_income():
        pass

    def get_all_products(self, product_name):
        for i in self.stock:
            if i[2] == product_name:
                print('')





if __name__ == '__main__':

    p1 = Product("fruit", "banana", 50)
    p2 = Product("food", "ramen", 20)
    p3 = Product('sport', 'ball', 3)
    s = ProductStore()
    s.add(p1, 10)
    s.add(p2, 300)
    s.add(p3,24)
    s.set_discount("banana", 0.7)
    s.sell_product("banana",3)

"""

    def sell_product(product_name, amount)

    def get_income():

    def get_all_products():

    def get_product_info(self, product_name):


"""
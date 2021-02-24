"""Lesson 12 Task 1

Method overloading.
Create a base class named Animal with a method called talk and then create two subclasses:
Dog and Cat, and make their own implementation of the method talk be different. For instance,
Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.
"""


class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return 'Woof woof'


class Cat(Animal):
    def talk(self):
        return 'meow'


def animal_talk(animal):
    print(animal.talk())


if __name__ == '__main__':
    cat = Cat()
    dog = Dog()
    animal_talk(cat)
    animal_talk(dog)

"""Task 2

Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books

```

class Library:
    pass

class Book:
    pass

class Author:
    pass

```
"""


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f'Name: {self.name}\n Country: {self.country}\n Birthday: {self.birthday}\n Books: {self.books}'

    def __repr__(self):
        return f'{self.name}'


class Book:
    book_count = 1

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.book_count += 1

    def __str__(self):
        return f'Name: {self.name}\n Year: {self.year}\nAuthor: {self.author}'

    def __repr__(self):
        return f'{self.name}'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __str__(self):
        return f'Name: {self.name}'

    def __repr__(self):
        return f'{self.name}'

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        if book not in self.books:
            self.books.append(book)
        if book not in author.books:
            author.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author):
        if author in self.authors:
            return author.books

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]


if __name__ == '__main__':
    p1 = Author('Petro', 'Ukraine', '01012010')
    p2 = Author('Vasyl', 'Poland', '01121900')
    p3 = Author('Oleh', 'Greece', '01111992')
    p4 = Author('Ihor', 'France', '04111990')
    my_library = Library('my_library')
    my_library.new_book('Sapiens', 1998, p1)
    my_library.new_book('Master', 1968, p2)
    my_library.new_book('Idiot', 1968, p3)
    my_library.new_book('Dictionary', 1976, p4)
    print(my_library)
    print(my_library.group_by_author(p1))
    print(my_library.group_by_year(1968))

"""
Task 3

Fraction

Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate checking and error handling

```

class Fraction:

pass

x = Fraction(1/2)

y = Fraction(1/4)

x + y == Fraction(3/4)

"""


def hhh(numenator, dominator):
    while dominator:
        numenator, dominator = dominator, numenator % dominator
    return numenator

class Fraction:
    def __init__(self, numenator: int, dominator: int):
        if not isinstance(numenator, int) and not isinstance(dominator, int):
            raise TypeError("write int")
        if dominator == 0:
            raise ZeroDivisionError("the dominator cant be zero")
        self.top = numenator
        self.bottom = dominator

    def __str__(self):
        if self.bottom == 1:
            return self.top
        elif self.top >= self.bottom:
            return f'{self.top} // {self.bottom} {self.top % self.bottom} / {self.bottom}'
        else:
            return f'{self.top}/{self.bottom}'

    def __add__(self, other):
        newtop = self.top * other.bottom + other.top * self.bottom
        newbottom = self.bottom * other.bottom
        common = hhh(newtop, newbottom)
        return f'{newtop // common}/{newbottom // common}' if abs(newtop // common) != abs(
            newbottom // common) else (newtop // common) // (newbottom // common)

    def __sub__(self, other):
        newtop = self.top * other.bottom - other.top * self.bottom
        newbottom = self.bottom * other.bottom
        common = hhh(newtop, newbottom)
        return f'{newtop // common}/{newbottom // common}' if abs(newtop // common) != abs(
            newbottom // common) else (newtop // common) // (newbottom // common)

    def __mul__(self, other):
        return f'{self.top * other.top}/{self.bottom * other.bottom}'

    def __truediv__(self, other):
        return f'{self.top * other.top}/{self.bottom * other.bottom}'

if __name__ == '__main__':

    x = Fraction(2,3)
    y = Fraction(1,2)
    print(y)
    print('sum', x + y)
    print('mult', x - y)
    print('sub', x * y)
    print('div', x / y)
g
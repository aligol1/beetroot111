"""Lesson 14 Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
 "add called with 4, 5"

def logger(func):
    pass

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]"""



def logger(func):
    def wraper(*args):
        print(f'{func.__name__} called with {args}')
        return func(*args)
    return wraper

@logger
def add(*args):
    return sum(arg for arg in args)

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == '__main__':
    add(5, 6)
    square_all(8, 9, 10)

"""Lesson 14 Task 2
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):
    pass
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
"""
StopList = ['pepsi', 'BMW']

def stop_words(words:list):
    def replace_word(func):
        def wraper(*args):
            text = func(*args)
            for word in words:
                text = text.replace(word, '*')
            return text
        return wraper
    return replace_word

@stop_words(StopList)
def create_slogan(name: str, lastname: str):
    return f'{name} {lastname} drinks pepsi in his brand new BMW!'

if __name__ == '__main__':
    print(create_slogan('john','Wick'))

"""Task 3
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise,
return the result.
```
def arg_rules(type_: type, max_length: int, contains: list):
    pass
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
"""


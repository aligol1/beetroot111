def subtraction(args):
    pass


if __name__ == '__main__':
    # LESSON 1
    # task 1
    s = "ку"
    print(s * 2, sep="-")
    print("My name is igor and I Should write my first program", end="!!!")
    # тут будет мой первый комментарий. комментировать пока нечего
    print("мне скоро")
    print(10 + 10 + 8, "лет")
    print("родился в 22/12/1992", end="\n\n\n")
    # проверяю абзацы
    print("space check", end="\n\n\n")
    print(
        "The Zen of Python, by Tim Peters \nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!")
    print()


    # task 2
    a = "#\t\t#"
    b = ("#"*9)
    print(b)
    print(a)
    print(a)
    print(a)
    print(b)
    print()
    print(a)
    print(a)
    print(b)
    print(a)
    print(a)
    print()

    # LESSON 2
    # task 1 GREETING PROGRAM

    name = "Igor"
    day = "19 December"
    print(f"Good day {name}!\n {day} is a perfect day to learn some python")

    # task 3 calculator
    print()
    print()
    print("калькулятор")
    a = 45
    b = 23
    c = 2
    print('addition')
    print(a + b + c)
    print('subtraction')
    print(a - b - c)
    print('division')
    print(a / b / c)
    print('multiplication')
    print(a * b * c)
    print('exponentiation')
    print(a ** b ** c)
    print('modulus')
    print(a % b)
    print('Floor division')
    print(a // b)

print()
print()
print()
print()

# task 2 Greeting
first_name = "Igor"
second_name = "Alergush"
print(f"Hello {first_name} {second_name} is a perfect day to learn some python.")

#задания со звездочкой

    print("{:05},{},{:b},{}".format(12, "Василий", 54, 32.1))

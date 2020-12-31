def subtraction(args):
    pass


if __name__ == '__main__':

    # Lesson 4 Task 1 The Guessing Game.
    # Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
    # The result should be sent back to the user via a print statement.

    import random
    randomnumber = random.randint(1, 10)
    print(randomnumber)
    player = str(input("Угадай число от 1 до 10: "))
    if player.isdigit() == True:
        player = int(player)
        if player == randomnumber:
            print("You win, the number is ", randomnumber)
        elif player > randomnumber or player < randomnumber:
            print("Your number is not ", randomnumber)
    else:
        print("You entered the wrong data. Please enter number between 1 and 10")

    #Lesson 4 Task 2 The birthday greeting program.
    #Write a program that takes your name as input, and then your age as input and greets you with the following:
    #“Hello <name>, on your next birthday you’ll be <age+1> years”

    user_name = input("What is your name?")
    user_age = input("How old are you?:")
    print("Hi ", user_name, "next year your age will be ", int(user_age) + 1, " years!")

    #Lesson 4 Task 3 Words combination
    #Create a program that reads an input string and then creates and prints 5 random strings
    # from characters of the input string.
    # For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
    # that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
    # Tips: Use random module to get random char from string)

    import random
    user_word = str.lower(input("введите слово: "))
    if not user_word.isalpha():
        print("Слово должно состоять из букв")
    else:
        randomized_letters = random.sample(user_word, len(user_word))
        print(''.join(randomized_letters)) #Так и не смог сделать пять разных вариаций. Только один рандом получился.


    #Lesson 4 Task 4 The math quiz program
    #Write a program that asks the answer for a mathematical expression, checks
    # whether the user is right or wrong, and then responds with a message accordingly.
    import random

    a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
    a1, a2 = random.choice(['+', '-', '*']), random.choice(['+', '-', '*'])
    if a1 == '+' and a2 == '+':
        result = a + b + c
    elif a1 == '+' and a2 == '-':
        result = a + b - c
    elif a1 == '+' and a2 == '*':
        result = a + b * c
    elif a1 == '-' and a2 == '+':
        result = a - b + c
    elif a1 == '-' and a2 == '-':
        result = a - b - c
    elif a1 == '-' and a2 == '*':
        result = a - b * c
    elif a1 == '*' and a2 == '+':
        result = a * b + c
    elif a1 == '*' and a2 == '-':
        result = a + b - c
    elif a1 == '*' and a2 == '*':
        result = a * b * c
    answer1 = int(input(f'Решите задачу: {a} {a1} {b} {a2} {c}:'))
    if answer1 == result:
        print("Good job")
    else:
        print("correct number is", result, " .Try again later")




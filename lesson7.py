if __name__ == '__main__':
    '''Lesson 7 Task 1  A simple function.
    Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. 
    The function should then print “My favorite movie is named {name}”.'''

    def favorite_movie(movie):
        print("My favorite name is: ", movie)

    name = input("what is your favorite movie?: ")
    favorite_movie(name)

    '''Lesson 7 Task 2
    Creating a dictionary. 
    Create a function called make_country, which takes in a country’s name and capital as parameters. 
    Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys. 
    Make the function print out the values of the dictionary to make sure that it works as intended.
    '''

    def make_country(country, capital):
        country_dictation = {'country': country, 'capital': capital}
        return country_dictation
    def print_dictat(d):
        print(d.values())
    if __name__=="__main__":
        dat = make_country("Ukraine", "Kiev")
        print_dictat(dat)


'''Lesson 7 Task 3 A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic 
operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) 
and an arbitrary number of arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter. For example:
the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  '''


    def make_operation(a_operator, num1, *args):
        return_value = num1
        if a_operator in ('+', '-', '*'):
            for number in args:
                if a_operator == '+':
                    return_value += number
                elif a_operator == '-':
                    return_value -= number
                else:
                    return_value *= number
            print(return_value)
        else:
            print("operator is wrong, please use + - or * ")

        make_operation('+', 5, 10)







    '''Lesson 8 Task 1
Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error. 
What happens if you change oops to raise KeyError instead of IndexError?
'''
def oops(anyerr):
    if anyerr == IndexError:
        raise anyerr


def itry():
    strtry = input("print here:")
    try:
        for i in range(len(strtry)+1):
            print(strtry[i])
    except IndexError:
        err = IndexError
        oops(err)
    else:
        print('something wrong')
    finally:
        print('ok')

if __name__ == '__main__':
    itry()

'''Lesson 8 Task 2
Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which raises
an exception if the two values given by the input function were not numbers, 
and if value b was zero (cannot divide by zero).   
'''
def devide(a, b):
    try:
        di = int(a)**2/int(b)
        print('%.2f' % di)
    except ValueError:
        print('use numbers')
        raise
    except ZeroDivisionError:
        print('dont use zero')
        raise


a = input('print divid. to squere')
b = input('enter divider')
devide(a, b)



#lesson 22 taks 2
def is_palindrome(a):
    if len(a) <= 1:
        return True
    if a[0] != a[-1]:
        return False
    return is_palindrome(a[1:-1])

if __name__ == '__main__':

    print(is_palindrome('mom'))
    print(is_palindrome('sassas'))
    print(is_palindrome('o'))
    print(is_palindrome('goglg'))

#lesson 22 task 3
def mult(a,n):
    if n == 0:
        return 0
    else:
        return a + mult(a, n - 1)


if __name__ == '__main__':
    a = 2
    b = 4
    print(mult(a,b))


#lesson 22 task 4
def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]

if __name__ == '__main__':

    mystr = "hello"
    print("дали: ", mystr)
    print("перевернули: ", reverse(mystr))

#lesson 22 task 5
def sum_of_digit(n):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))

if __name__ == '__main__':
    num = 282
    result = sum_of_digit(num)
    print("сумма цифр в ", num, "будет", result)



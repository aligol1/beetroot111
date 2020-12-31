if __name__ == '__main__':

    '''Lesson 5 Task 1 
    The greatest number
    Write a Python program to get the largest number from a list of random numbers with the length of 10
    Constraints: use only while loop and random module to generate numbers'''

    import random
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)
    d = random.randint(1, 100)
    e = random.randint(1, 100)
    maxchislo = max(a, b, c, d, e)
    print(maxchislo)

'''Lesson 5 Task 2 
Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10,
and make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers'''

import random
    a_list = random.sample(range(1, 10), 5)
    b_list = random.sample(range(1, 10), 5)
    c_list = set(a_list + b_list)
    print(c_list)


    '''Lesson 5 Task 3
    Extracting numbers.
    Make a list that contains all integers from 1 to 100, 
    then find all integers from the list that are divisible by 7 but not a multiple of 5, 
    and store them in a separate list. Finally, print the list.
    Constraint: use only while loop for iteration
    '''
    other = [i for i in range(1, 101) if i % 5 != 0 and i % 7 == 0]
    print(other)


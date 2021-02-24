"""Lesson 26 Task1
Task 1

A bubble sort can be modified to “bubble” in both directions.
The first pass moves “up” the list and the second pass moves “down.”
This alternating pattern continues until no more passes are necessary.
Implement this variation and describe under what circumstances it might be appropriate."""


def bubble(number):
    n = len(number)

    for i in range(n):

        for ia in range(0, n - i - 1):
            if number[ia] > number[ia + 1]:
                number[ia], number[ia + 1] = number[ia + 1], number[ia]

number = [5, 7, 1, 4, 5, 457, 12]
bubble(number)
for i in range(len(number)):
    print(number[i])
"Lesson 13 Taks 1 Write a Python program to detect the number of local variables declared in a function."

def my_func():
    a, b = 1, 2
    my_list = [1, 2, 3]
    sum_list = [i for i in my_list]
    my_str = "yui"
    my_dict = {}

print(f' The number of local var declared in a func {my_func.__name__}:{my_func.__code__.co_lnotab}')


"Lesson 13 Task 2 Write a Python program to access a function inside a function (Tips: use function, which returns another function)"

def make_sum_numbers_to_power(power):
    def sum_numbers(*args):
        return sum(num**power for num in args)
    return sum_numbers

if __name__ == '__main__':
    pw = make_sum_numbers_to_power(3)
    print(pw(3, 4, 5, 6))


'''Lesson Task 3'''

"""Write a function called `choose_func` which takes a list of nums and 2 callback functions. 
If all nums inside the list are positive, execute the first function on that list and return the result of it. 
Otherwise, return the result of the second one

def choose_func(nums: list, func1, func2):
    pass
# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
def square_nums(nums):
    return [num ** 2 for num in nums]
def remove_negatives(nums):
    return [num for num in nums if num > 0]
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
"""

def choose_func(nums: list, func1, func2):
    if [num for num in nums if num < 0]:
        return func2(nums)
    else:
        return func1(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    print(choose_func(nums1, square_nums, remove_negatives))
    print(choose_func(nums2, square_nums, remove_negatives))
if __name__ == '__main__':
    '''Lesson 6 Task 1
Make a program that has some sentence (a string) 
on input and returns a dict containing all unique words as keys and the number of occurrences as values. '''

while True:
    user_slovo = (input("Введите слово: ").split())
    dictionary = {}
    for i in user_slovo:
        dictionary[i] = user_slovo.count(i)
    print(dictionary)

    ''''Task 2
    Create a function which takes as input two dicts with structure mentioned above,
    then computes and returns the total price of stock.'''

    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    total_price = {}
    total = 0
    for product_name, product_qty in stock.items():
        product_price = prices.get(product_name, 0)
        total_price[product_name] = product_qty * product_price
        total += product_qty + product_price
    print(f'total_price: {total_price} \ntotal: {total}')


    '''Task 3 List comprehension exercise'''

    list1 = [(i,i**2) for i in range(1,11)]
    print(list1)

    '''Task 4 with*'''
    weekdays = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    weekdays = {value: key for key, value in weekdays.items()}
    print(weekdays)
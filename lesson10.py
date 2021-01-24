'''Lesson 10 Task 1 A Person class
Make a class called Person.
Make the __init__() method take firstname,
lastname, and age as parameters and add them as attributes.
Make another method called talk() which makes prints a greeting from the person containing,
for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
'''

class Person:
    def __init__(self, firstname='Igor', lastname='Alergush', age=28):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        print(firstname,lastname,age)

    def talk(self):
        print('Hello, my name is ', self.firstname, self.lastname, 'and I’m ', self.age, 'years old')

firstperson = Person()
firstperson.talk()

'''Lesson 10 Task 2 Doggy age
Create a class Dog with class attribute `age_factor` equals to 7. 
Make __init__() which takes values for a dog’s age. 
Then create a method `human_age` which returns the dog’s age in human equivalent.'''

class Dog:
    age_factor = 7

    def __init__(self, dogage):
        self.dogage = dogage

    def human_age(self):
        return self.dogage * self.age_factor

igor = Dog(14)
igor.human_age()
print(igor.human_age())


'''Lesson 10 Task 3 TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N 
or 'name' exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

```
CHANNELS = ["BBC", "Discovery", "TV1000"]
 class TVController:
pass
 controller = TVController(CHANNELS)
controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"
```'''

channels = ['BBC', '1+1', 'CNN', 'TV1000', 'MTV', 'Ictv']

class TVComtroller:
    channel = 0

    def __init__(self, ch):
        self.position = 0
        self.choose_channel = ch

    def first_channel(self):
        self.position = 0
        return self.current_channel()

    def last_channel(self):
        self.position = len(self.choose_channel)-1
        return self.current_channel()

    def current_channel(self):
        return self.choose_channel[self.position]

    def next_channel(self):
        if self.position != len(self.choose_channel)-1:
            self.position += 1
        else:
            self.position = 0
        return self.current_channel()

    def turn_channel(self, number):
        self.position = number-1
        return self.current_channel()

    def previous_channel(self):
        if self.position != 0:
            self.choose_channel -= 1
        else:self.position = len(self.choose_channel) -1
        return self.current_channel()

    def is_exist(self, search_channel):
        if search_channel in range(1, len(self.choose_channel)+1) or search_channel in self.choose_channel:
            answer: 'yes'
        else:
            answer: 'no'
            return answer

if __name__ == "__main__":
    controller = TVComtroller(channels)
    print(controller.first_channel())
    print(controller.last_channel())
    print(controller.turn_channel(4))
    print(controller.next_channel())
    print(controller.current_channel())
    print(controller.is_exist(4)) ####### НЕ ПОНИМАЮ ПОЧЕМУ НЕ РАБОТАЕТ
    print(controller.is_exist('MTV')) ####### НЕ ПОНИМАЮ ПОЧЕМУ НЕ РАБОТАЕТ


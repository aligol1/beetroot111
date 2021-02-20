#Lesson 24 task 2 Implement a stack using a singly linked list.
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):

        if self.isempty():
            return None

        else:
            popnode = self.head
            self.head = self.head.next
            popnode.next = None
            return popnode.data

    def showme(self):

        mydata = self.head
        if self.isempty():
            print("nichego net")

        else:

            while (mydata != None):
                print(mydata.data, "->", end=" ")
                aaa = mydata.next
            return


MyStack = Stack()
MyStack.push(1)
MyStack.push(2)
MyStack.push(3)
MyStack.push(4)
MyStack.pop()
MyStack.pop()
MyStack.showme()
print(MyStack.isempty())


# Lesson 24 Task 3
# Implement a queue using a singly linked list.


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.nachalo = self.konec = None

    def isEmpty(self):
        return self.nachalo == None

    def AddtoQueue(self, item):
        a = Node(item)

        if self.konec == None:
            self.nachalo = self.konec = a
            return
        self.konec.next = a
        self.konec = a

    def RemoveQueue(self):

        if self.isEmpty():
            return
        temp = self.nachalo
        self.nachalo = temp.next

        if (self.nachalo == None):
            self.konec = None


if __name__ == '__main__':
    q = Queue()
    q.AddtoQueue(1)
    q.AddtoQueue(2)
    q.RemoveQueue()
    print(str(q.nachalo.data))
    q.AddtoQueue(3)
    q.AddtoQueue(4)
    q.AddtoQueue(5)
    q.RemoveQueue()
    print("Queue Nachalo " + str(q.nachalo.data))
    print("Queue Konec " + str(q.konec.data))
    print(q.isEmpty())
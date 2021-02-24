#Lesson 24 Task 3
#Implement a queue using a singly linked list.


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None




# The queue, front stores the front node
# of LL and rear stores the last node of LL
class Queue:

    def __init__(self):
        self.nachalo = self.konec = None

    def isEmpty(self):
        return self.nachalo == None

    def AddtoQueue(self, item):
        temp = Node(item)

        if self.konec == None:
            self.nachalo = self.konec = temp
            return
        self.konec.next = temp
        self.konec = temp

        # Method to remove an item from queue

    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.nachalo
        self.nachalo = temp.next

        if (self.nachalo == None):
            self.konec = None


# Driver Code
if __name__ == '__main__':
    q = Queue()
    q.AddtoQueue(1)
    q.AddtoQueue(2)
    q.DeQueue()
    q.AddtoQueue(3)
    q.AddtoQueue(4)
    q.AddtoQueue(5)
    q.DeQueue()
    print("Queue Front " + str(q.nachalo.data))
    print("Queue Rear " + str(q.konec.data))

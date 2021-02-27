# Lesson 28 task 1
#Implement a binary heap as a max heap.


def heapify(arr, n, i):
    largest = i;
    l = 2 * i + 1;
    r = 2 * i + 2;

    if l < n and arr[l] > arr[largest]: #если левое больше чем рут
        largest = l;


    if r < n and arr[r] > arr[largest]: #если правое больше чем рут
        largest = r;

    if largest != i: # если наибольшее не рут
        arr[i], arr[largest] = arr[largest], arr[i];

        heapify(arr, n, largest);


def buildheap(arr, n):

    startIdx = n // 2 - 1;  # индекс последней нон лиф ноды

    for i in range(startIdx, -1, -1): # обход в обратном от последнего
        heapify(arr, n, i);

def printheap(arr, n):
    for i in range(n):
        print(arr[i], end=" ");

if __name__ == '__main__':
    arr = [11, 23, 25, 44, 64, 134, 120, 10, 899, 125, 1713];
    n = len(arr);
    buildheap(arr, n);
    printheap(arr, n);
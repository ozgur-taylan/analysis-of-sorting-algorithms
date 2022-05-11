# inputs
import random

# ex: [0,1,2,3,4,5,...,n]
sorted_list_1 = list(range(0,1))
sorted_list_10 = list(range(0,10))
sorted_list_50 = list(range(0,50))
sorted_list_100 = list(range(0,100))
sorted_list_500 = list(range(0,500))
sorted_list_1000 = list(range(0,1000))
sorted_list_5000 = list(range(0,5000))
sorted_list_7500 = list(range(0,7500))
sorted_list_9900 = list(range(0,9900))

# ex: [n,n-1,n-2,...,1,0]
reverse_sorted_1 = sorted_list_1[::-1]
reverse_sorted_10 = sorted_list_10[::-1]
reverse_sorted_50 = sorted_list_50[::-1]
reverse_sorted_100 = sorted_list_100[::-1]
reverse_sorted_500 = sorted_list_500[::-1]
reverse_sorted_1000 = sorted_list_1000[::-1]
reverse_sorted_5000 = sorted_list_5000[::-1]
reverse_sorted_7500 = sorted_list_7500[::-1]
reverse_sorted_9900 = sorted_list_9900[::-1]

# ex: [n,n,n,n,n,...,n]
equal_list_1 = [1 for x in range(1)]
equal_list_10 = [10 for x in range(10)]
equal_list_50 = [50 for x in range(50)]
equal_list_100 = [100 for x in range(100)]
equal_list_500 = [500 for x in range(500)]
equal_list_1000 = [1000 for x in range(1000)]
equal_list_5000 = [5000 for x in range(5000)]
equal_list_7500 = [7500 for x in range(7500)]
equal_list_9900 = [9900 for x in range(9900)]

# ex: [random, random, random,...,random]
duplicate_random_1 = [random.randrange(5) for i in range(1)]
duplicate_random_10 = [random.randrange(5) for i in range(10)]
duplicate_random_50 = [random.randrange(5) for i in range(50)]
duplicate_random_100 = [random.randrange(10) for i in range(100)]
duplicate_random_500 = [random.randrange(50) for i in range(500)]
duplicate_random_1000 = [random.randrange(100) for i in range(1000)]
duplicate_random_5000 = [random.randrange(500) for i in range(5000)]
duplicate_random_7500 = [random.randrange(750) for i in range(7500)]
duplicate_random_9900 = [random.randrange(990) for i in range(9900)]

# ex: [0,1,2,3,67,43,2,3,10]
semi_sorted_1 = list(range(0,1))

semi_sorted_10 = list(range(0,10))
semi_sorted_10[4:] = [random.randrange(10) for i in range(6)]

semi_sorted_50 = list(range(0,50))
semi_sorted_50[15:] = [random.randrange(50) for i in range(35)]

semi_sorted_100 = list(range(0,100))
semi_sorted_100[20:] = [random.randrange(100) for i in range(80)]

semi_sorted_500 = list(range(0,500))
semi_sorted_500[100:] = [random.randrange(500) for i in range(400)]

semi_sorted_1000 = list(range(0,1000))
semi_sorted_1000[200:] = [random.randrange(1000) for i in range(800)]

semi_sorted_5000 = list(range(0,5000))
semi_sorted_5000[1000:] = [random.randrange(5000) for i in range(4000)]

semi_sorted_7500 = list(range(0,7500))
semi_sorted_7500[2500:] = [random.randrange(7500) for i in range(5000)]

semi_sorted_9900 = list(range(0,9900))
semi_sorted_9900[4000:] = [random.randrange(9900) for i in range(5900)]

## Heapsort ##
def heapify(arr, size, i):
    global x
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    x = x + 1
    if (left < size and arr[largest] < arr[left]):
        largest = left

    x = x + 1
    if (right < size and arr[largest] < arr[right]):
        largest = right

    if (largest != i):
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp

        heapify(arr, size, largest)

def heapSort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp

        heapify(arr, i, 0)


## Merge Sort ##
def mergeSort(arr):
    if (len(arr) > 1):
        global x
        x = x + 1
        m = len(arr) // 2

        l = arr[:m]
        r = arr[m:]

        mergeSort(l)
        mergeSort(r)

        i = 0
        j = 0
        k = 0

        while (i < len(l) and j < len(r)):
            x = x + 1
            if (l[i] < r[j]):
                arr[k] = l[i]
                i = i + 1

            else:
                x = x + 1
                arr[k] = r[j]
                j = j + 1
            k = k + 1

        while i < len(l):
            arr[k] = l[i]
            i = i + 1
            k = k + 1

        while j < len(r):
            arr[k] = r[j]
            j = j + 1
            k = k + 1

## Insertion Sort ##
def InsertionSort(arr):
    n = 0
    j = 0
    for x in range(1, len(arr)):
        n += 1
        forw = arr[x]
        back = x - 1
        while back >= 0 and arr[back] > forw:
            j += 1
            arr[back + 1] = arr[back]
            back = back - 1
        arr[back + 1] = forw


    return arr

## Counting Sort ##
def CountingSort(array):
    first = 0
    sec = 0
    third = 0
    fourth = 0

    max_element = max(array)
    size = len(array)

    output = [0] * size
    count = [0] * (max_element + 1)

    for i in range(0, size):
        count[array[i]] += 1
        first += 1

    for i in range(1, max_element + 1):
        count[i] += count[i - 1]
        sec += 1

    i = size - 1
    while i >= 0:
        third += 1
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        fourth += 1
        array[i] = output[i]


    return array

## Binary Insertion Sort ##
def BinarySearchLocation(arr, start, end, number, iteration):
    mid = int((start + end) / 2)

    if end >= start:
        if number == arr[mid]:
            return iteration, mid
        elif number > arr[mid]:
            iteration += 1
            return BinarySearchLocation(arr, mid + 1, end, number, iteration)
        elif number < arr[mid]:
            iteration += 1
            return BinarySearchLocation(arr, start, mid - 1, number, iteration)
    else:
        if number > arr[mid]:
            return iteration, mid + 1
        else:
            return iteration, mid


def BinaryInsertionSort(arr):
    iter_outer = 0
    iter_inner = 0
    iteration = 0
    for i in range(1, len(arr)):
        number = arr[i]
        iteration, index = BinarySearchLocation(arr, 0, i - 1, number, 0)
        iter_outer += 1
        for j in range(i, index, -1):
            iter_inner += 1
            arr[j] = arr[j - 1]
        arr[index] = number


    return arr


def main():
    ## inputs to show that codes are working ##
    test1 = [2,7,5,3,6,1,69,31]
    test2 = [2,7,5,3,6,1,69,31]
    test3 = [2,7,5,3,6,1,69,31]
    test4 = [2,7,5,3,6,1,69,31]
    test5 = [2,7,5,3,6,1,69,31]

    ## By giving different inputs that has been created above as a parameter, results can be observed.

    InsertionSort(test1)
    BinaryInsertionSort(test2)
    CountingSort(test3)
    heapSort(test4)
    mergeSort(test5)

    print(test1)
    print(test2)
    print(test3)
    print(test4)
    print(test5)

main()
#####################################################################################################
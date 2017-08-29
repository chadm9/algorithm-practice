

lyst = [2,6,8,2,3,9,7,0,1,3]
#
# lyst2  = [1,2,3,4,5,6,7,8]

def bubbleSort(lyst):
    switched = False
    times_through = 0

    for i in range(len(lyst) - 1):
        for j in range(len(lyst) - (times_through+1)):

            if lyst[j] > lyst[j+1]:
                switched = True
                first_element = lyst[j]
                second_element = lyst[j+1]
                lyst[j] = second_element
                lyst[j+1] = first_element
        times_through += 1
        if switched == False:
            return lyst


    return lyst

for i in range(len(lyst) - 1):
    bubbleSort(lyst)

print bubbleSort(lyst)


lyst = [2,6,8,2,3,9,7,0,1,3]


def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i + 1:])
        first_part.append(x[i])
        return first_part + second_part


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# print quicksort(alist)
# print(alist)

def merge_sort(array):
    ret = []
    if( len(array) == 1):
        return array;
    half  = len(array) / 2
    lower = merge_sort(array[:half])
    upper = merge_sort(array[half:])
    lower_len = len(lower)
    upper_len = len(upper)
    i = 0
    j = 0
    while i != lower_len or j != upper_len:
        if( i != lower_len and (j == upper_len or lower[i] < upper[j])):
            ret.append(lower[i])
            i += 1
        else:
            ret.append(upper[j])
            j += 1

    return ret

array = [4, 2, 3, 8, 8, 43, 6,1, 0]
ar = merge_sort(array)
print " ".join(str(x) for x in ar)


# =======================================================================
#  Author: Isai Damier
#  Title: Heapsort
#  Project: geekviewpoint
#  Package: algorithms
#
#  Statement:
#  Given a disordered list of integers (or any other items),
#  rearrange the integers in natural order.
#
#  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
#  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
#
#  Time Complexity of Solution:
#  Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n)).
#
#  Approach:
#  Heap sort happens in two phases. In the first phase, the array
#  is transformed into a heap. A heap is a binary tree where
#  1) each node is greater than each of its children
#  2) the tree is perfectly balanced
#  3) all leaves are in the leftmost position available.
#  In phase two the heap is continuously reduced to a sorted array:
#  1) while the heap is not empty
#  - remove the top of the head into an array
#  - fix the heap.
#  Heap sort was invented by John Williams not by B. R. Heap.
#
#  MoveDown:
#  The movedown method checks and verifies that the structure is a heap.
#
#  Technical Details:
#  A heap is based on an array just as a hashmap is based on an
#  array. For a heap, the children of an element n are at index
#  2n+1 for the left child and 2n+2 for the right child.
#
#  The movedown function checks that an element is greater than its
#  children. If not the values of element and child are swapped. The
#  function continues to check and swap until the element is at a
#  position where it is greater than its children.
# =======================================================================


def swap(i, j):
    sqc[i], sqc[j] = sqc[j], sqc[i]

def heapify(end,i):
    l=2 * i + 1
    r=2 * (i + 1)
    max=i
    if l < end and sqc[i] < sqc[l]:
        max = l
    if r < end and sqc[max] < sqc[r]:
        max = r
    if max != i:
        swap(i, max)
        heapify(end, max)

def heap_sort():
    end = len(sqc)
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end-1, 0, -1):
        swap(i, 0)
        heapify(i, 0)

sqc = [2, 7, 1, -2, 56, 5, 3]
heap_sort()
print(sqc)
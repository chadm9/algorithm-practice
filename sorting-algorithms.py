

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






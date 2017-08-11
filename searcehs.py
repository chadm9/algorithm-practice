
def linear_search(array, target):
    for element in array:
        if element == target:
            return True
    return False




# def linear_search_recursive(array, target):
#     if len(array) == 0:
#         return False
#     if array[0] == target:
#         return True
#     else:
#         del array[0]
#         return linear_search_recursive(array, target)


def linear_search_recursive(array, target, index=0):
    if len(array) == index:
        return False
    if array[index] == target:
        return True
    else:
        return linear_search_recursive(array, target, index+1)


my_array = [1,2,3,20]


def binary_search(array, value):
    midpoint = len(array)/2
    right_end = len(array) - 1
    left_end = 0

    while (right_end >= left_end):
        if array[midpoint] > value:
            right_end = midpoint - 1
            midpoint = (left_end+right_end)/2
        elif array[midpoint] < value:
            left_end = midpoint + 1
            midpoint = (left_end+right_end)/2
        else:
            return True


    return False

my_array = [1,2,3,20]

def binary_search_recursive(array,value,left,right):

    midpoint = (left+right)/2
    if array[midpoint] == value:
        return True
    elif left >= right:
        return False
    else:
        if array[midpoint] > value:
            return binary_search_recursive(array, value, left, midpoint - 1)
        else:
            return binary_search_recursive(array, value, midpoint + 1, right)

for i in range(21):
    print binary_search(my_array, i)



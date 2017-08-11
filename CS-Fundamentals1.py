

def bubble_sort(my_array):
    switched = False
    times_through = 0
    for i in range(len(my_array) - 1):
        for j in range(len(my_array) - (1 + times_through)):

            if my_array[j] > my_array[j+1]:
                switched = True
                first_element = my_array[j]
                my_array[j] = my_array[j+1]
                my_array[j+1] = first_element

        if not switched:
            return my_array

        times_through += 1

    return my_array


# input_arrays = [
# [],
# [9, 8, 7, 6, 5, 4, 3, 2, 1],
# [1, 2, 3, 4],
# [4, 6, 1, 3, 7, 8, 4, 3, 4],
# [1],
# [1, 3, 2]
# ]
#
#
# for array in input_arrays:
#     print("")
#     print(" Input: " + str(array))
#     sorted_array = bubble_sort(array)
#     print("Output: " + str(sorted_array))

# def sum_of_multiples():
#     sum = 0
#     for i in range(1000):
#         if ((i%3 == 0) or (i%5 == 0)):
#             sum += i
#
#     return sum

# def triangle_numbers(n):
#
#     return n*(n-1)/2


lyst = [2,6,8,2,3,9,7,0,1,3]


# def insertionSort(lyst):
#     for i in range(1, len(lyst)):
#         value_to_move = lyst[i]
#         j = i
#
#         while j > 0 and lyst[j-1] > value_to_move:
#             lyst[j] = lyst[j-1]
#             j -= 1
#
#         lyst[j] = value_to_move
#
#     return lyst

# def insertion_sort(my_array):
#
#     for i in range(1, len(my_array)):
#         temp = my_array[i]
#         j = i
#         while j > 0 and my_array[j-1] > temp:
#             my_array[j] = my_array[j-1]
#             j -= 1
#
#         my_array[j] = temp
#
#
#
#     return my_array
#
#
# input_arrays = [
# [],
# [9, 8, 7, 6, 5, 4, 3, 2, 1],
# [1, 2, 3, 4],
# [4, 6, 1, 3, 7, 8, 4, 3, 4],
# [1],
# [1, 3, 2]
# ]
# for array in input_arrays:
#     print("")
#     print(" Input: " + str(array))
#     sorted_array = insertion_sort(array)
#     print("Output: " + str(sorted_array))



# print insertionSort(lyst)



# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
import datetime
def run_program():
    MAX = 50000000
    sum = 0
    for i in range(1, MAX):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    print("The sum of all the multiples of 3 or 5 below " + str(MAX) + " is " + str(sum) + ".")

start_time = datetime.datetime.now()
run_program()
end_time = datetime.datetime.now()
duration = end_time - start_time
print("This program ran in " + str(duration))
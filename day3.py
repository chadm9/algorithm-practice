# def square_and_sort(sorted_list):
#     # if the list is empty, there is nothing to do. just return the list.
#     if len(sorted_list) == 0:
#         return sorted_list
#
#     # if the first number is positive, square the list and sort it.
#     if sorted_list[0] >= 0:
#         for i in range(len(sorted_list)):
#             sorted_list[i] *= sorted_list[i]
#         return sorted_list
#
#     # if the last number is negative, reverse the list.
#     if sorted_list[len(sorted_list) - 1] <= 0:
#         new_list = []
#         for i in reversed(sorted_list):
#             new_list.append(i * i)
#         return new_list
#
#     # If we get to this point, our array has both
#     # negative and positive values.
#
#     # STEP 1: Find the inflection index
#     inflection_index = None
#
#     for i in range(1, len(sorted_list)):
#         if sorted_list[i - 1] < 0 and sorted_list[i] >= 0:
#             if abs(sorted_list[i - 1]) < abs(sorted_list[i]):
#                 inflection_index = i - 1
#             else:
#                 inflection_index = i
#             break
#
#     # STEP 2: Square and sort.
#     left = inflection_index - 1
#     right = inflection_index + 1
#
#     new_sorted_list = [sorted_list[inflection_index] * sorted_list[inflection_index]]
#     # Keep looping as long as the left index is >= than -1
#     # AND the right index is < the size of the original array
#     while(left >= -1 and right < len(sorted_list)):
#         if left == -1:
#             new_sorted_list.append(sorted_list[right] * sorted_list[right])
#             right += 1
#         elif right == len(sorted_list) - 1:
#             new_sorted_list.append(sorted_list[left] * sorted_list[left])
#             left -= 1
#         else:
#             if abs(sorted_list[left]) < abs(sorted_list[right]):
#                 new_sorted_list.append(sorted_list[left] * sorted_list[left])
#                 left -= 1
#             elif abs(sorted_list[left]) >= abs(sorted_list[right]):
#                 new_sorted_list.append(sorted_list[right] * sorted_list[right])
#                 right += 1
#
#     return new_sorted_list
#
# def run_example(a_list):
#     print('input: ' + str(a_list))
#     print('output: ' + str(square_and_sort(a_list)))
#     print('\n')
#
# run_example([-20, -9, 0, 10, 21])
# run_example([1, 2, 3, 4, 5])
# run_example([-5, -4, -3, -2, -1])


def frequent_integer(array):

    freq_dict = {}

    for i in range(0, len(array)-1):
        if not freq_dict.has_key(array[i]):
            freq_dict[array[i]] = 1

        else:
            freq_dict[array[i]] += 1

    max_key = None
    max_value = -1
    for key in freq_dict:

        if freq_dict[key] > max_value:
            max_value = freq_dict[key]
            max_key = key

    return max_key


lyst = [1,1,1,1,3,2,3,3]

print frequent_integer(lyst)
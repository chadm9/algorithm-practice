def permutations(array):

    # If the array is empty then there are no permutations
    if len(array) == 0:
        return []

    # If there is only one element in the array, only
    # one permuatation is possible
    if len(array) == 1:
        return [array]

    final_list = [] # empty list that will store all permutations

    # Iterate the array and calculate the permutation
    for i in range(len(array)):
       value_to_hold_in_place = array[i]

       # Extract the value_to_hold_in_place from the list. Remaining list is the rest of the numbers
       remaining_elements = array[:i] + array[i+1:]

       # Generate all permutations where value_to_hold_in_place is
       # the first element
       for p in permutations(remaining_elements):
           final_list.append([value_to_hold_in_place] + p)
    return final_list


# data = list('12345')
# p = permutations(data)
# for permutation in p:
#     print(permutation)


print(type('hat') != str)

def reverse_string(input):
    result = ''
    for i in range(len(input)-1, -1, -1):
        result += input[i]
    return result

print reverse_string('hat')

test = [1,2,3,4,5]

print(test[2:])
print(test[:3])
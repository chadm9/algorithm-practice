# def my_hash_function(value):
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#     result = letters.index(value[0])
#     return result
#
#
# def numberhash(value):
#     result = ''
#     for i in range(3):
#         result += value[i]
#
#     return result
#
#
#
# print(my_hash_function('doc'))
# print(my_hash_function('carrot'))
#
# print(numberhash('770-592-6781'))




# def is_palindrome(input):
#     for i in range(len(input)/2):
#         if(input[i] == input[-1 - i]):
#             pass
#         else:
#             return False
#
#     return True
#
#
# print is_palindrome('doooooooood')


class MyNode:
    def __init__(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = MyNode(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node

    def remove(self, value):
        current_node = self.head

        while (current_node.value != value and current_node != None):
            current_node = current_node.next_node

        if current_node == None:
            return False

        next_node = current_node.next_node
        previous_node = current_node.previous_node
        next_node.previous_node = previous_node
        previous_node.next_node = next_node
        return True

    def insert(self, value, index):
        new_node = MyNode(value)
        i = 0
        current_node = self.head

        while (i != index - 1 and current_node != None):
            current_node = current_node.next_node
            i += 1

        if current_node == None:
            return self.append(value)

        next_node = current_node.next_node
        next_node.previous_node = new_node
        current_node.next_node = new_node
        new_node.next_node = next_node
        new_node.previous_node = current_node

    def exists(self, value):
        current_node = self.head


        while (current_node.value != value and current_node != None):
            current_node = current_node.next_node


        if current_node == None:
            return False

        return True


class MyHashTable:
    def __init__(self):
        self.buckets = [None] * 26

    def hash(self, value):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        first_letter = value[0]
        return alphabet.index(first_letter.lower())

    def insert(self, value):
        new_node = MyNode(value)
        insert_to = self.hash(value)


        if self.buckets[insert_to] == None:
            new_linked_list = MyLinkedList()
            new_linked_list.append(value)
            self.buckets[insert_to] = new_linked_list


            self.buckets[insert_to].append(value)


    def exists(self, value):
        array_index = self.hash(value)
        if self.buckets[array_index] == None:
            return False

        return self.buckets[array_index].exists(value)





hash_table = MyHashTable()
hash_table.insert('Hello World')
hash_table.insert('Bob')
hash_table.insert('Cathy')
hash_table.insert('Zebra')

print(hash_table.exists('Hello World'))
print hash_table.buckets[1].tail.value
print(hash_table.buckets)


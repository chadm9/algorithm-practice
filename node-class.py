class MyNode:
    def __init__(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None

node1 = MyNode(5)
node2 = MyNode(10)
node1.next_node = node2

# print(node1.next_node.value)

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
        while(current_node.value != value and current_node.next_node != None):
            # print current_node.value, current_node.next_node.value
            current_node = current_node.next_node

        if current_node == None:
            return False

        next_node = current_node.next_node
        previous_node = current_node.previous_node
        previous_node.next_node = next_node
        return True



    def removeAll(self, value):
        pass

    def insert(self, value, index):
        new_node = MyNode(value)
        current_node = self.head
        current_index = 0
        while(current_index < index and current_node != None):
            current_node = current_node.next_node
            current_index += 1

        if current_node.value == None:
            return self.append(value)

        # new_next_node = current_node
        new_node.previous_node = current_node.previous_node
        new_node.next_node = current_node
        current_node.previous_node.next_node = new_node
        current_node.previous_node = new_node





    def exists(self, value,index):
        pass

linked_list = MyLinkedList()
linked_list.append(10)
linked_list.append(15)
linked_list.append(20)
linked_list.insert(7,1)
print linked_list.head.next_node.value


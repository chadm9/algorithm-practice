class MyNode:
    def __init__(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None



class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def queue(self, value):
        new_node = MyNode(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node

    def dequeue(self):

        if self.head == None:
            return False
        else:
            self.head = self.head.next_node
            self.head.previous_node = None



class MyStack:
    def __init__(self):
        self.top = None
        self.bottom = None

    def push(self, value):
        new_node = MyNode(value)

        if self.top == None:
            self.top = new_node
            self.bottom = new_node

        else:
            self.top.next_node = new_node
            new_node.previous_node = self.top
            self.top = new_node

    def pop(self):

        if self.top == None:
            pass
        else:
            self.top = self.top.previous_node
            self.top.next_node = None


# linked_list = MyQueue()
# linked_list.queue(10)
# linked_list.queue(15)
# linked_list.queue(20)
# linked_list.dequeue()
# print linked_list.head.value

linked_list = MyStack()
linked_list.push(10)
linked_list.push(15)
linked_list.push(20)
linked_list.pop()
print linked_list.top.value
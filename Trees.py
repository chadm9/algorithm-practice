class BinaryTreeNode:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.value = value

    def print_nodes(self, prefix, indents):
        if indents == 0:
            indent = prefix
        else:
            indent = ""

        for i in range(indents):
            if i == indents - 1:
                indent += "\t" + prefix
            else:
                indent += "\t"

        print(str(indent) + ' ' + str(self.value))
        if self.left_child != None:
            self.left_child.print_nodes(' left:', indents + 1)
        if self.right_child != None:
            self.right_child.print_nodes('right:', indents + 1)

    def invert(self, current_node):
        if current_node == None:
            return None
        else:
            current_node.left_child, current_node.right_child = current_node.right_child, current_node.left_child
            self.invert(current_node.left_child)
            self.invert(current_node.right_child)


class MyBinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = BinaryTreeNode(value)

        if self.root == None:
            self.root = new_node
        else:
            # Traverse the tree and look for
            # the right place to insert the node.
            current_node = self.root

            while (True):
                if current_node.value > new_node.value:
                    if current_node.left_child == None:
                        current_node.left_child = new_node
                        new_node.parent = current_node
                        break
                    else:
                        current_node = current_node.left_child
                else:
                    if current_node.right_child == None:
                        current_node.right_child = new_node
                        new_node.parent = current_node
                        break
                    else:
                        current_node = current_node.right_child

    def exists(self, value):
        if self.root == None:
            return False

        new_node = BinaryTreeNode(value)
        current_node = self.root

        while(current_node != None):
            if current_node.value == new_node.value:
                return True
            else:
                if current_node.value > new_node.value:
                    current_node = current_node.left_child
                else:
                    current_node = current_node.right_child

        return False


    def exists_recursion(self, value, current_node):
        if self.root == None:
            return False


        if current_node == None:
            return False
        elif current_node.value == value:
            return True
        elif current_node.value > value:
            return self.exists_recursion(value, current_node.left_child)
        else:
            return self.exists_recursion(value, current_node.right_child)

    def invertTree(self):
        current_node = self.root
        current_node.invert(current_node)





    def print_tree(self):
        if self.root != None:
            self.root.print_nodes(' root:', 0)


tree = MyBinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(15)

tree.print_tree()
tree.invertTree()
print
tree.print_tree()

# print tree.exists_recursion(1, tree.root)
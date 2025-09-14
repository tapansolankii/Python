class Node:
    def __init__(self, value):
        self.value = value
        self.children = []  # List to hold child nodes


class Tree:
    def __init__(self):
        self.root = None  # Start with an empty tree

    def add_child(self, parent, child):
        parent.children.append(child)

    def display(self, node, level=0):
        print("  " * level + str(node.value))
        for child in node.children:
            self.display(child, level + 1)


# Create Nodes
root = Node("Root")
child1 = Node("Child 1")
child2 = Node("Child 2")
grandchild = Node("Grandchild 1")

# Build Tree
tree = Tree()
tree.root = root
tree.add_child(root, child1)
tree.add_child(root, child2)
tree.add_child(child1, grandchild)

# Display Tree
tree.display(root)


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\12_basicTree.py
# Root
#   Child 1
#     Grandchild 1
#   Child 2
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> 
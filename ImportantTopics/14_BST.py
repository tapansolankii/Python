from collections import deque

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def search(self, root, value):
        if not root:
            return None
        if value == root.value:
            return root
        elif value<root.value:
            return self.search(root.left, value)
        return self.search(root.right, value)
    
    def insert(self, root, value):
        if root is None:
            return BinarySearchTree(value)
        elif value<root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root
    
    def print_bst(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.value))
            if root.left or root.right:  # Print branches only if they exist
                if root.left:
                    self.print_bst(root.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")

                if root.right:
                    self.print_bst(root.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")



root = None
root = BinarySearchTree(50)
root.insert(root, 30)
root.insert(root, 70)
root.insert(root, 20)
root.insert(root, 40)
root.insert(root, 60)
root.insert(root, 80)

# Search
result = root.search(root, 40)
print("Found" if result else "Not Found")


root.print_bst(root)




# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\14_BST.py
# Found
# Root: 50
#     L--- 30
#         L--- 20
#         R--- 40
#     R--- 70
#         L--- 60
#         R--- 80
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> 
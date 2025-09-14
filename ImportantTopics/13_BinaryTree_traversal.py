from collections import deque

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=" ")
            self.inorder_traversal(root.right)

    
    def preorder_traversal(self, root):
        if root:
            print(root.value, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)


    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.value, end=" ")


    def level_order_traversal(self, root):
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.value, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)



root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

print("Inorder Traversal:")
root.inorder_traversal(root)

print("\nPreorder Traversal:")
root.preorder_traversal(root)

print("\nPostorder Traversal:")
root.postorder_traversal(root)

print("\nLevel Order Traversal:")
root.level_order_traversal(root)



# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\13_BinaryTree.py
# Inorder Traversal:
# 4 2 5 1 3 
# Preorder Traversal:
# 1 2 4 5 3 
# Postorder Traversal:
# 4 5 2 3 1 
# Level Order Traversal:
# 1 2 3 4 5 
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> 
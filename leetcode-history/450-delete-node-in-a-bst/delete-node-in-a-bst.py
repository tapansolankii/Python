class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
           
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            successor = self.getMin(root.right)
           
            root.val = successor.val
           
            root.right = self.deleteNode(root.right, successor.val)
            
        return root

    def getMin(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr
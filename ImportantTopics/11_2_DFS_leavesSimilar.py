# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Helper function to find leaf nodes
        def getLeaves(root):
            leaves = []
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    # If it's a leaf node, add to the result
                    if not node.left and not node.right:
                        leaves.append(node.val)
                    # Add right and left children for DFS traversal
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
            return leaves
        
        # Get leaf sequences for both trees
        leaves1 = getLeaves(root1)
        leaves2 = getLeaves(root2)
        
        # Compare the sequences
        return leaves1 == leaves2


# Create Tree 1
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right = TreeNode(1)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)

# Create Tree 2
root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right = TreeNode(1)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

# Test the function
solution = Solution()
result = solution.leafSimilar(root1, root2)
print(result)  # Output: True



# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\11_DFS_leavesSimilar.py
# True
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> 
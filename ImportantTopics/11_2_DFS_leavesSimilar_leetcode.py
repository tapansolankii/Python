# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(root):
            leaves = []
            stack = [root]
            # print(stack)
            while stack:
                node = stack.pop()
                print(node)
                if node:
                    if not node.left and not node.right:
                        leaves.append(node.val)
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
            return leaves
        leaves1 = getLeaves(root1)
        print()
        print()
        print()
        leaves2 = getLeaves(root2)
        return leaves1 == leaves2






# Accepted
# Runtime: 0 ms
# Case 1
# Input
# root1 =
# [3,5,1,6,2,9,8,null,null,7,4]
# root2 =
# [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Stdout
# TreeNode{val: 3, left: TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}}}, right: TreeNode{val: 1, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}}
# TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}}}
# TreeNode{val: 6, left: None, right: None}
# TreeNode{val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}}
# TreeNode{val: 7, left: None, right: None}
# TreeNode{val: 4, left: None, right: None}
# TreeNode{val: 1, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}
# TreeNode{val: 9, left: None, right: None}
# TreeNode{val: 8, left: None, right: None}



# TreeNode{val: 3, left: TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, right: TreeNode{val: 1, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 2, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}}}
# TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}
# TreeNode{val: 6, left: None, right: None}
# TreeNode{val: 7, left: None, right: None}
# TreeNode{val: 1, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 2, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}}
# TreeNode{val: 4, left: None, right: None}
# TreeNode{val: 2, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}
# TreeNode{val: 9, left: None, right: None}
# TreeNode{val: 8, left: None, right: None}
# View less
# Output
# true
# Expected
# true







# Case 2
# Accepted
# Runtime: 0 ms
# Case 1
# Case 2
# Input
# root1 =
# [1,2,3]
# root2 =
# [1,3,2]
# Stdout
# TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}
# TreeNode{val: 2, left: None, right: None}
# TreeNode{val: 3, left: None, right: None}



# TreeNode{val: 1, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 2, left: None, right: None}}
# TreeNode{val: 3, left: None, right: None}
# TreeNode{val: 2, left: None, right: None}
# View less
# Output
# false
# Expected
# false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        max_sum = -float('inf')
        max_level=0
        current_level=1
        while queue:
            length_level = len(queue)
            sum_level = 0
            for _ in range(length_level):
                node = queue.popleft()
                sum_level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if sum_level>max_sum:
                max_sum = sum_level
                max_level=current_level
            current_level+=1
        return max_level
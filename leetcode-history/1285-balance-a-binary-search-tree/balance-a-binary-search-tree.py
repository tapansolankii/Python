class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        sorted_vals = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        
        def build_balanced_tree(left, right):
            if left > right:
                return None
            
            
            mid = (left + right) // 2
            node = TreeNode(sorted_vals[mid])
            
            
            node.left = build_balanced_tree(left, mid - 1)
            node.right = build_balanced_tree(mid + 1, right)
            
            return node
            
        return build_balanced_tree(0, len(sorted_vals) - 1)
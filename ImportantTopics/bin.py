def goodNodes(self, root: TreeNode) -> int:
    def dfs(node, max_val):
        if not node:
            return 0
        count=0 if node.val>=max_val else 0
            
        max_val=max(node.val,max_val)

        count+=dfs(node.left,max_val)
        count+=dfs(node.right,max_val)
        return count
    return dfs(root, root.val)

def goodNodes(self, root: TreeNode) -> int:
    # Helper function for DFS traversal
    def dfs(node, max_val):
        if not node:
            return 0
        
        # Check if the current node is "good"
        count = 1 if node.val >= max_val else 0
        
        # Update the maximum value along the path
        max_val = max(max_val, node.val)
        
        # Recur for left and right subtrees
        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)
        
        return count
    
    # Start DFS from root with its value as the initial max
    return dfs(root, root.val)
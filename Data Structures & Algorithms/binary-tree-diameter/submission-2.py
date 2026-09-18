# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(node):
            if not node:
                return 0
            
            # look at 2 to 5 and 2 to 4 for example
            # makes it easy to visualize

            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal res 
            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return res
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # if tree doesn't exist, return null
        # recursive DFS
        # start from root
        # recurse down both sides
        # dfs(curr)
        # base case: if node returns null, return null
        # if curr. node is either p or q, return it
        # if left and right recursion returns non-null, LCA is the curr. node
        # if p and q are in diff. subtrees, then the LCA will be the root node where they split
        # Time: O(n)
        # Space: O(h)

        curr = root

        def dfs(curr):
            if not curr:
                return None
            
            if curr == p or curr == q:
                return curr
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left and right:
                return curr

            if not left and not right:
                return None
            
            if not left and right or left and not right:
                return left if left else right
        
        return dfs(root)

            
            



        
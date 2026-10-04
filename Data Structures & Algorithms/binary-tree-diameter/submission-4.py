# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # at each node, longest path through node is left height + right height

        # dfs(curr) -> height of subtree rooted at curr.
        # if curr is null, return 0 height
        # recurse left and right, update max variable
        # return height

        diam = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal diam
            diam = max(diam, left + right)
            return 1 + max(left, right) # so parent knows how tall subtree is
        
        dfs(root)
        return diam
        


        
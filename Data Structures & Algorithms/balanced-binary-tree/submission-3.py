# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # store boolean and height -> [isBalanced, height]

        # node is balanced if both l and r subtrees balanced, and height diff <= 1

        # run DFS on root, return isBalanced

        def dfs(root):

            if not root:
                return [True, 0] # balanced by default w/ height 0
            
            left, right = dfs(root.left), dfs(root.right) # recurse

            # balanced check
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])] 
        
        return dfs(root)[0] # True or False

        

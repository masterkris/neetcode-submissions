# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # don't need BFS
        # curr = root
        # low, high approach
        # could do a DFS recursive approach
        # dfs (node, left, right)
        # base case: if null, return True
        # if node is outside bounds, return False
        # left child -> recurse (node->left, left, parent) -> upper bound becomes parent, left bound becomes same
        # right child -> recurse (node->right, parent, right) -> lower bound becomes parent
        # main idea: every node has to respect all ancestor limits
        # Runtime: O(n) time, O(h) space
        
        def dfs(node, left, right):
            if not node:
                return True

            # left and right are ultimate boundaries
            if not (left < node.val < right): # range of vals. of the BST
                return False 

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right) # node.val will be the parent
    
        curr = root
        return dfs(curr, -float("inf"), float("inf"))


        
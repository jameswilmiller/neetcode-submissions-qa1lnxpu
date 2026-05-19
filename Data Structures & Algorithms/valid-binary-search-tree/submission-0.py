# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # ok we want to dfs, we pass currentMin and CurrentMax to each call
        # we check if the left child val is less than current min
        # we check that the right child val is greater than current max

        def dfs(node, left, right):
            # if node is empty we return true
            if not node:
                return True
            # if the val is not between the min and the max it is invalid 
            if not (left < node.val < right):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right
            )

        return dfs(root, float("-inf"), float("inf"))
            
            
            
            
            
        
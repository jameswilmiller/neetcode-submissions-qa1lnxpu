# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we dfs each child + greatest value we have seen so far 

        def dfs(node, maxVal):
            if not node:
                return 0
            
            # is current node good node or not?
            res = 1 if node.val >= maxVal else 0

            # update max value
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)


         

        
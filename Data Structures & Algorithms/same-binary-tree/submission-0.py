# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we are going to use DFS to search the tree, at each step in recursion we want to check
        # if the current nodes are either null or have same value, if one is null and other isnt
        # or the dont have same value return false if values match recursively check left and right subtrees
        # if any recursive call returns false the result is false
      
        
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
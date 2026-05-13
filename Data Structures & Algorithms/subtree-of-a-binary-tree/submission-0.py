# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        
        if not t:
            return True
        
        if not s:
             return False

        #if they are the same tree return true
        if self.sameTree(s, t):
            return True
        
        #compare t to left and right subtree of s
        return (self.isSubtree(s.left, t)
        or self.isSubtree(s.right, t))

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left,  t.left) and
                    self.sameTree(s.right, t.right))
        return False






        

        

        
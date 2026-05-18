# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we want to bfs to get an array for each level and return the right most value for each level?
        
        # we add root node to queue
        # we store a result array 
        # we look at the right most value of our q
        # we add it to our result
        

        # now we look at the child of the current node and add them to the q
        # we pop the left of the queue
        # now we add right most value of the level to the result 
        # now we pop left and add the children to the queue
        # we need to remove what is left in the queue and add its children
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            # our q at any point contains a whole level
            qLen = len(q)
            # for every element in the initial length
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                res.append(rightSide.val)

        return res




        
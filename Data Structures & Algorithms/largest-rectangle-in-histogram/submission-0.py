class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #largest rectangle given barheights where all have width of 1
        #if height in decreasing order can pop 
        #if height is equal or increasing can contiuously move right
        #then once we reached decreasing compute area and pop and move to next rectangle

        #basically move from left to right i.e start on left pillar check if next is higher if it is 
        #continue checking until reaching pillar that is lower height, once u have reached compute area 
        #and move to next pillar
        #because we pop most recent heights being considered we should use a stack

        ## algorithm:
        # add index and height to a stack
        # if the height of an element is lower then current top of stack:
        # pop the stack until it is empty and calculate the height as final (index - initial index) * initial height
        maxArea = 0
        stack = [] # pair (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

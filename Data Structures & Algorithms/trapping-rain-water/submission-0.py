class Solution:
    def trap(self, height: List[int]) -> int:
        #need to take min of the max left height and max right height - current height

        #we need max left and max right height for each position
        #we need to calculate min(l, r) for each position
        #first scan the array and calculate maxleft and maxright for each position
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
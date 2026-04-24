class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if middle >= leftmost value, then search left
        # else search right

        
        l = 0
        r = len(nums) - 1
        minNum = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minNum = min(minNum, nums[l])
                break

            m = ((l + r) // 2)
            minNum = min(nums[m], minNum)
            if nums[m] >= nums[l]:
                l = m + 1
                
            else:
                r = m - 1
                
        return minNum
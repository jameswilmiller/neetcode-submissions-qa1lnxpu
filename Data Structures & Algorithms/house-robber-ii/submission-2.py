class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def solveLinear(arr):
            memo = {}
            def maxRob(i):
                if i >= len(arr):
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(arr[i] + maxRob(i+2), maxRob(i + 1))
                return memo[i]
            return maxRob(0)

        if len(nums) == 1:
            return nums[0]
            
        slice1 = nums[1:]
        slice2 = nums[:len(nums) - 1]

        return max(solveLinear(slice1), solveLinear(slice2))   
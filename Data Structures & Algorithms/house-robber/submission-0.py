class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def maxRob(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + maxRob(i + 2), maxRob(i + 1))
            return memo[i]
        return maxRob(0)


        
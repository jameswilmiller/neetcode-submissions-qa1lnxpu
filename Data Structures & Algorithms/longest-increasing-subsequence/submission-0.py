class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #starting at index i what is longest increasing subsequence
        memo = {}

        def solve(i):
            best = 1
            if i in memo:
                return memo[i]
                
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + solve(j))
            memo[i] = best
            return memo[i]
            
        
        res = float("-inf")

        for i in range(len(nums)):
            res = max(res, solve(i))

        return res
            
        
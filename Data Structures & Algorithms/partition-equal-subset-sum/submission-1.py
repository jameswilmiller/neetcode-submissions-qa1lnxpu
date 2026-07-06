class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0
        for num in nums:
            total_sum += num
        if total_sum % 2 != 0:
            return False 

        target = total_sum // 2
        memo = {}
        def solve(i, remaining):
            if remaining == 0:
                return True
            if i == len(nums):
                return False

            # skip
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            skip = solve(i + 1, remaining)
            # include
            including = solve(i + 1, remaining - nums[i])
            # return 
            memo[(i, remaining)] = skip or including
            return memo[(i, remaining)]
        return solve(0, target)


            
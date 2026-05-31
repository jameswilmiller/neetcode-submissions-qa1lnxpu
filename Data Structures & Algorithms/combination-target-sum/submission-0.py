class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        combination = []
        def dfs(i):
            #first check if combination exceeds target
            
            if sum(combination) > target:
                return
            
            if sum(combination) == target:
                res.append(combination.copy())
                return
            
            if i >= len(nums):
                return 
            #choice 1 stay at current number
            combination.append(nums[i])
            dfs(i)

            #choice 2
            combination.pop()
            dfs(i + 1)

        dfs(0)
        return res



        
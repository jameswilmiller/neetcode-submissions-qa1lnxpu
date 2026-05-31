class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # i is index of value we are making decision on
        subset = []
        def dfs(i):
            #check out of bounds
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
            




       

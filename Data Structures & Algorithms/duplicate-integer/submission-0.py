class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #iterate over list once and fill in hashmap, if element is unseen add
        #if element is seen, break and return true
        #if loop completes return false
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen[nums[i]] = i
        return False
        
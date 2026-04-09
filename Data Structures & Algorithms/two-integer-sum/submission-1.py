class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #goal return the indexes of the two numbers i, j that add to target
        
        #for each number check the target - number and then check if that exists in the hashmap
        #the hashmap should have number as key and index as value 
        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i
        
            
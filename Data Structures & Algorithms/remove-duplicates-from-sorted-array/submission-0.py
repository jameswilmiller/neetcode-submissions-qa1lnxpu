class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         #two pointers 
         #right pointer scans the array
         #left tells us where to put each unique value
         #we can determine a value is unique by comparing to previous value

         #first I am going to initiliase L and R pointer at index 2 because first value will be same

        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
        
                
        
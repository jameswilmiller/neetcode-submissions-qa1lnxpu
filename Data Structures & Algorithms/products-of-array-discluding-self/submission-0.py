class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #store prefix and suffix in seperate arrays i.e product of everything to left of current index is prefix product of everything right is suffix
        #all prefix products excluding self in one array and all suffix excluding self in another
        #goal prefix[i] = product of everything left of i
        #goal suffix[i] = product of everything right of i
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

        
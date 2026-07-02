class Solution:
    def countSubstrings(self, s: str) -> int:
        
        memo = {}
        def isPalindrome(i, j):
            if i >= j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            res = (s[i] == s[j]) and (isPalindrome(i+1, j-1))
            memo[(i, j)] = res
            return res
        
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    count += 1
        return count

        
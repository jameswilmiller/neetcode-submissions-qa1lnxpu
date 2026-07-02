class Solution:
    def longestPalindrome(self, s: str) -> str:
        # what are my choices? 
        memo = {}
        def isPalindrome(i, j):
            # base case we have i == j
            if i >= j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            result = (s[i] == s[j]) and isPalindrome(i+1, j-1)
            memo[(i, j)] = result
            return result
                
        best = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j) and (j - i + 1) > len(best):
                    best = s[i: j+1]
        return best
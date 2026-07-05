class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        # lets start with 
        def solve(i):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]

            for word in wordDict:
                if s[i : i + len(word)] == word:
                    if solve(i + len(word)):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return False
        return solve(0)
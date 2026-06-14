class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substring = []
        def dfs(i):
            if i >= len(s):
                # add the substring to res
                res.append(substring.copy())
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    substring.append(s[i:j+1])
                    dfs(j + 1)
                    substring.pop()
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

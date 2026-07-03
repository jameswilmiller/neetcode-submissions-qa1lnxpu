class Solution:
    def numDecodings(self, s: str) -> int:
        # for each digit, we can either check it is a single digit decoding
        # or we can skip it and check for a double digit encoding
        
        memo = {}

        def numWays(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            
            ways_from_one_digit = numWays(i + 1)

            ways_from_two_digits = 0
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways_from_two_digits = numWays(i + 2)
            
            memo[i] = ways_from_one_digit + ways_from_two_digits
            return memo[i]
        return numWays(0)
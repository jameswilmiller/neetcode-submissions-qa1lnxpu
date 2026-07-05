class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # starting at  the amount we can choose each type of coin
        # what is the base case? if we go down the tree and get negative we return 0
        # if we go down the tree and get to 0 then we return 1
        # we do a tree starting by subtracting each type of coin and 
       
        memo = {}

        def minCoin(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1   
            if remaining in memo:
                return memo[remaining]
            best = float('inf')

            for coin in coins:
                result = minCoin(remaining - coin)
                if result != -1:
                    best = min(best, 1 + result)
            memo[remaining] = best if best != float('inf') else -1
            return memo[remaining]
        
        return minCoin(amount)

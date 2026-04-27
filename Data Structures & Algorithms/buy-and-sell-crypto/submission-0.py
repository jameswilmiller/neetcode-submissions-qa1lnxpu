class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #2 ptr
        # l = buy
        # r = sell
        # track max profit

        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            #check if profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


        
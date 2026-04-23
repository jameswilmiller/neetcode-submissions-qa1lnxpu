class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #each hour choose a pile and eat k banans if pile has less than k consume the pile
        #trying brute force first
        # try k from 1..max(pile) first value we get that allows all piles to be eaten in less than h is output
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += (math.ceil(p / k))
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res


        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        maxi = 0
        buy = prices[0]
        sell = 0

        for x in prices:
            if x < buy:
                buy = x
                sell = 0
            if sell < x:
                sell = x
                maxi = max(maxi, sell - buy)

        return maxi
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float("inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                buy[i] = min(buy[i], price - sell[i - 1])
                sell[i] = max(sell[i], price - buy[i])

        return sell[k]
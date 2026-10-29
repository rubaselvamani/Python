'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.
'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

if __name__ == "__main__":
    prices = [1,2,3,4,5,6,7,8]
    #prices = [1,0,0,0,0,0]
    a = Solution()
    print(a.maxProfit(prices))


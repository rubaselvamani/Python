'''
Maximum revenue from K consecutive orders

Find the maximum revenue generated from any k consecutive orders.
'''

class Solution:
    def best_revenue(self,revenues:list,k:int) -> int:

        if k<=0 or k> len(revenues):
            return 0

        window_revenue = sum(revenues[:k])
        max_revenue = window_revenue

        for right in range(k,len(revenues)):
            window_revenue += revenues[right]
            window_revenue -= revenues[right-k]
            max_revenue = max(max_revenue,window_revenue)

        return max_revenue

if __name__ == "__main__":
        a = Solution()
        print(a.best_revenue([100, 200, 150, 300, 250],2))




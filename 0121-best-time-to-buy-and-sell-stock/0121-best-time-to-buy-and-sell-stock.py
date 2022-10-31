class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        profit = 0
        
        for price in prices:
            profit = max(price - min_price, profit)
            
            if price < min_price:
                min_price = price
            
            
        return profit
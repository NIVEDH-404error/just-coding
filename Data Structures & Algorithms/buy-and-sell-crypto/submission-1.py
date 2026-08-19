class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        max_price=0
        for i,curr in enumerate(prices):
            if i==0 or buy>curr:
                buy=curr
                print("buy if",buy)
                print("curr if",curr)
                print("max if",max_price)
                print("profit current if",curr-buy)

            elif buy<curr:
                max_price=max(max_price,curr-buy)
                print("buy",buy)
                print("curr",curr)
                print("max",max_price)
                print("profit current",curr-buy)
        return max_price


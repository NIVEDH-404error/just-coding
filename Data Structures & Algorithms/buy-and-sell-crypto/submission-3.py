class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        profit=0
        '''for i,curr in enumerate(prices):
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
                print("profit current",curr-buy)'''
        for i,curr in enumerate(prices): #0 #7
            if i==0 or curr < buy: #0 #7 <#0
                buy=curr

            elif buy<curr:
                profit=max(profit,curr-buy)

        return profit
        


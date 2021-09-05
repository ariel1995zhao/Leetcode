class Solution:
    ## solution1: Brute force, time complexity O(N^2)

    ## two pointer
    ## [7,1,5,3,6,4]
    ##  B
    ##    S-> 

    ##    B 
    ##      S-> 
    
    
    
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        profit = 0 
        for i in range(len(prices)-1):
            sell = prices[i+1]
            for j in range(i+1,len(prices)):
                buy = prices[i]
                if prices[j] > buy and prices[j] >= sell:
                    sell = prices[j]
                    profit = max(profit, sell-buy)
        return profit


class Solution:
    ## solution2: 
    ## [7,4,5,1,3,6,4]
    ##              i 
    ##       GM
    ##           MP=5

    ## One index walk through global minimum, one index loop through the array 

    ## Time: O(N)
    
    
    
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices or len(prices) == 1:
            return 0 
        i = 1 
        globalMin = prices[0]
        maxProfit = 0
        while i < len(prices):
            if prices[i] < globalMin:
                globalMin = prices[i]

            else:
                maxProfit = max(maxProfit, prices[i]-globalMin)
            i+=1
            
        return maxProfit 
            
        
        
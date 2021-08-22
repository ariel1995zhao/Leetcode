from typing import List

# weights = [1,2,3,4,5,6,7,8,9,10]

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if not weights:
            return 
        left = max(weights)
        right = sum(weights)
        while left < right-1:
            mid = (left + right)//2
            if self.calculate(weights,mid) <= D:
                right = mid 
            else:
                left = mid 
        return left if self.calculate(weights,left) <= D else right 
        
        #return left if self.calculate(weights,mid) <= D else right 

    def calculate(self,weights, cap):
        ## calculate if use cap weights as the maximun capacity, how many days will it take
        day = 0
        temp = cap
        total = sum(weights)
        for i in range(len(weights)):
            if cap - weights[i] >= 0:
                total -= weights[i]
                cap -= weights[i]
            else:
                day += 1
                cap = temp - weights[i]
        return day + 1
        




from typing import List

# weights = [1,2,3,4,5,6,7,8,9,10]

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if not weights:
            return 
        left = max(weights)
        right = sum(weights)
        while left < right-1:
            mid = (left + right)//2
            if self.calculate(weights,mid) <= D:
                right = mid 
            else:
                left = mid 
        return left if self.calculate(weights,left) <= D else right 
        
        #return left if self.calculate(weights,mid) <= D else right 

    def calculate(self,weights, cap):
        ## calculate if use cap weights as the maximun capacity, how many days will it take
        day = 0
        total = 0
        for w in weights:
            total += w
            if total > cap:
                day += 1
                total = w
        return day + 1
            
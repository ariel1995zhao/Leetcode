class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0 
        if x == 1:
            return 1
        left = 0
        right = x
        while left < right -1:
            mid = (left + right)//2
            if mid*mid > x:
                right = mid 
            elif mid * mid < x:
                left = mid
            else:
                return mid 
        if (right*right) > x and (left*left) < x:
            return left 



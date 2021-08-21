## leetcode 702 

class Solution:
    def search(self, reader, target: int) -> int:
        if not reader:
            return -1
        left = 0 
        right = 1
        while reader.get(right) < target:
            right *= 2
        while left + 1 < right:
            mid = (left + right) // 2
            val = reader.get(mid)
            if(val >= target):
                right = mid 
            else:
                left = mid 
        if reader.get(left) == target:
            return left 
        if reader.get(right) == target:
            return right 
        return -1
            
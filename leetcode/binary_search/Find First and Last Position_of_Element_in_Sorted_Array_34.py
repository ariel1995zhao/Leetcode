from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1,-1]
        
        first = -1
        last = -1
        left = 0 
        right = len(nums) -1

        ## find last occurance 
        
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid 
            else:
                right = mid 
        
        if nums[left] == target:
            last = left 
        if nums[right] == target:
            last = right 
        
        left = 0 
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid 
            else:
                left = mid 
        if nums[right] == target:
            first = right
        if nums[left] == target:
            first = left 
        if left == right == -1:
            return [-1,-1]
        return [first, last]

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums)-1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid 
                else:
                    left = mid 
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid 
                else:
                    right = mid 
        if nums[left] == target:
            return left 
        if nums[right] == target:
            return right 
        return -1
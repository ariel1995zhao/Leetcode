class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid
        if nums[left] == nums[right] == target:
            return left 
        if nums[right] < target:
            return (right + 1)
        elif nums[left] < target and nums[right] > target:
            return (left + 1)
        elif nums[left] >= target:
            return left
        elif nums[right] == target:
            return right 

            
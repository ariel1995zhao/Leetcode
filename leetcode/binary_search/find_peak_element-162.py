class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 
        left = 0 
        right = len(nums)-1
        while left < right - 1:
            mid = (left + right)// 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid 
            elif nums[mid] < nums[mid+1]:
                left = mid 
            else:
                right = mid 
        return left if (nums[left] > nums[right]) else right 
                
        
class Solution:

    ## in place switch 
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return 
        slow = 0 ## store non-zero in the left
        fast = 1  ## look for zero 
        while fast <= len(nums)-1:
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
                fast += 1
                if fast > len(nums)-1:
                    return nums
            
            if nums[slow] == nums[fast] == 0:
                fast += 1
        
            if nums[slow] != 0 and nums[fast] == 0:
                fast += 1
                slow += 1

            elif nums[slow] != 0 and nums[fast] != 0:
                slow += 1
                fast += 1

        return nums



## Solution 2: 遇到非0 数字直接覆盖到0 的位置，然后把0 加到最后


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0 
        fast = 0 
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast] 
                slow += 1
            fast += 1
        
        while slow < len(nums):
            nums[slow] = 0 
            slow += 1
        return nums
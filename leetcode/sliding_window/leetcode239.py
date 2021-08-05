class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k <= 0:
            return None
        if k == 1:
            return nums
        output_array = []
        temp_max = float('-inf')
        for i in range(len(nums)):
            if i + k <= len(nums):
                for j in range(i, i + k):
                    if nums[j] > temp_max:
                        temp_max = nums[j]
                output_array.append(temp_max)
                temp_max = float('-inf')
        return output_array


## exceed time limit

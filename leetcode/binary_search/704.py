class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if target is None:
            return -1
        left = 0 
        right = len(nums)-1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
    


## time complexity: O(logN)

## memory complexity: O(1)


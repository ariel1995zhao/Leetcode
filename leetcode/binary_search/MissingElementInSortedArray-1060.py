## Binary Search Approach 

from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1
        while left < right - 1:
            mid = (left + right) // 2
            diff = nums[mid] - nums[left] - (mid - left)
            if diff >= k:
                right = mid 
            else:
                left = mid 
                k = k - diff 
        if nums[left] + k >= nums[right]:
            return nums[left] + k + 1
        else:
            return nums[left] + k 


## Dictionary approach


from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 
        
        ret = []
        for index in range(len(nums)-1):
            
            if len(ret) >= k:
                return ret[k-1]
            
            left = nums[index]
            right = nums[index+1]
            
            for i in range(left+1,right):
                ret.append(i)
        
        length = len(ret)
        base = nums[-1]
        
        while length < k:
            base += 1
            ret.append(base)
            length += 1
        
        return ret[k-1]
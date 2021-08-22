from typing import List
## Two sum: 
## solution 1: dictionary. Make every index in dictionary, 
##.           let target - index and check if it's in Dict
##            Space: O(N), time(n)

## solution 2: sort and two pointer, one at most left, one at most right 
##            Space: O(1), time O(NlogN + N)

## 3 Sum: sort first,then have a pointer move from left to right, make it as target 
##        for the rest 2 indexes. Have another 2 indexes point to the left and right 
##        If greater than the target, then right-1. If smaller than the target.
##        then left +1. Until we find a match for the target, then return the 3 indexes


## [-1,0,1,2,-1,-4]
## [-4,-1,-1,0,1,2]
##   i 
##      L        R
##         L     R --> append 
##           L   R
##             L R
## =====================
## [-4,-1,-1,0,1,2]
##      i 
##         L     R --> append
##           L R
##           L R
##             L R
## =====================
## [-4,-1,-1,0,1,2]
##         i 
##            L  R
##            L R --> append 
##            R L
##            



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -1 * nums[i]
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return ans
      
      
      
      
      
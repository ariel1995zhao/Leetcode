class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    ## [0,1,3,0,4,0,4,2]  -> [0,1,3,0,4,2,2,2]
    ##                i
    ##            c 
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count 


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    ## [0,1,2,2,3,0,4,2]  -> [0,1,3,0,4,2,2,2]
    ##          i
    ##      j
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1
        return j 
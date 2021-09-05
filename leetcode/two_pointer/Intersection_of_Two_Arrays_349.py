from typing import List

## [1,2,2,1]
##  i
## [2,2]
##  j


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ## brute force, time complexity O(N^2)
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if nums1[i] not in result:
                        result.append(nums1[i])
        return result
        


class Solution:

    ## two pointer 
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ## two pointer
        ## [1,2,2,1]      [2,2]
        ##  i              j
        ## nums_set
        ## if nums1[i] not in nums_set: then append. if in nums_set, then append to result
        i = 0 
        j = 0 
        nums_set = set()
        common = set()
        
        for i in range(len(nums1)):
            if nums1[i] not in nums_set:
                nums_set.add(nums1[i])
            i += 1
        
        for j in range(len(nums2)):
            if nums2[j] in nums_set and nums2[j] not in common:
                common.add(nums2[j])
            j+= 1
        
        return list(common)


class Solution:
    # HashSet - O(n + m)时间，O(n)空间
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
                
        
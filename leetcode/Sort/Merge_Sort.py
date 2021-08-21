
## physical meaning: split the array in half, sort the left part, and sort the right part, then merge them in one

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums 
        middle = (len(nums)+1)//2
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])
        result = merge(left,right)
        return result 
    
    def merge(self,left,right):
        new_list = []
        i = 0 
        j = 0
        while i< len(left) and j < len(right):
            if left[i] < right[j]:
                new_list.append(left[i])
                i+=1
            else:
                new_list.append(right[j])
                j += 1
        while i < len(left):
            new_list.append(left[i])
            i += 1
        
        while j < len(right):
            new_list.append(right[j])
            j += 1
        return new_list



## Time complexity: O(NlogN)
## Space complexity: O(N)
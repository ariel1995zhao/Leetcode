from random import randrange

## Find Pivot and swap the number smaller to the pivot to the left, and swap the number larger than pivot to the right

## Partition: traverse the array, put the number smaller than pivot in the left, put the number larger than pivot in the right. After it's done, then the pivot is in the middle. 

## Store_index 物理含义：第一个比pivot 大的数字的index；swap 过后，就是pivot 新的index

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        start = 0 
        end = len(nums)-1
        return self.quick_sort(nums,start,end)
    
    def quick_sort(self,nums, start,end):
        if start >= end:
            return
        pivot_index = randrange(start,end+1)
        new_pivot_index = self.partition(nums,start,end,pivot_index)
        self.quick_sort(nums,start,new_pivot_index-1)
        self.quick_sort(nums,new_pivot_index+1,end)
        return nums
    
    def partition(self,nums,start,end,pivot_index):
        nums[pivot_index],nums[end] = nums[end],nums[pivot_index]
        store_index = start
        pivot = nums[end]
        for i in range(start,end):
            if nums[i] < pivot:
                nums[i],nums[store_index] = nums[store_index],nums[i]
                store_index += 1
        nums[store_index],nums[end] = nums[end],nums[store_index]
        return store_index



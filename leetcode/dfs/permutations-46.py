from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        res = list()
        temp = list()
        is_visited = [False for _ in range(len(nums))]
        self.dfs(res,temp,is_visited,nums)
        return res 
        
    
    def dfs(self,res,temp,is_visited,nums):
        if(len(temp) == len(nums)):
            res.append(temp[:])
            return 
        
        for i in range(len(nums)):
            if is_visited[i]:
                continue
            temp.append(nums[i])
            is_visited[i] = True
            self.dfs(res,temp,is_visited,nums)
            is_visited[i] = False
            print(temp)
            temp.pop()



            
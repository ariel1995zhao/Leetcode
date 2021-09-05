## combination sum 

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or not target:
            return []
        res = list()
        temp = list()
        self.dfs(res, temp, 0, candidates, target, 0)
        return res
             
    def dfs(self, res, temp, index, candidates, target, total):
        if target == total:
            res.append(temp[:])
            return
        if target < total:
            return
        for i in range(index, len(candidates)):
            temp.append(candidates[i])
            self.dfs(res, temp, i, candidates, target, total + candidates[i])
            temp.pop()






            
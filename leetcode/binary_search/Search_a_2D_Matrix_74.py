from typing import List

## solution 1, index conversion 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        left = 0 
        right = m*n - 1
        while left <= right:
            mid = (left + right) // 2
            row_index = mid // n 
            col_index = mid % n 
            if matrix[row_index][col_index] < target:
                left = mid +1 
            elif matrix[row_index][col_index] > target:
                right = mid - 1
            else:
                return True 
        return False 


        
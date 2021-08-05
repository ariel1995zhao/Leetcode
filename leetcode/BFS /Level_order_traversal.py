class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        while queue: # 
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                    
            ans.append(level)
        return ans
                

from typing import List
from collections import deque 
class Solution:


    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return []
        queue = deque()
        answer = []
        xBias = [-1,0,0,1]
        yBias = [0,1,-1,0]
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    fresh += 1
                elif(grid[i][j] == 2):
                    queue.append(i*n + j)
                    
        minute = 0
        while(len(queue) != 0 and fresh != 0):
            size = len(queue)
            level = []
            for i in range(size):
                rotting = queue.popleft()
                x = rotting // n
                y = rotting % n 
                for j in range(len(xBias)):
                    newX = x + xBias[j]
                    newY = y + yBias[j]
                    if(self.valid(grid,newX, newY)):
                        fresh -= 1
                        queue.append(newX*n + newY)
                        grid[newX][newY] = 2
            minute += 1
        return(minute if fresh == 0 else -1)
    
    def valid(self,grid, x,y):
        if x<0 or y<0 or x > (len(grid)-1) or y > (len(grid[0]) -1):
            return False
        if(grid[x][y] == 1):
            return True
        return False
# solution 1, recursion + for loop

from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        islands = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islands += 1
                    self.part_of_island(grid,i,j)
        return islands 
    
    def part_of_island(self,grid,i,j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1:
            return 
        else:
            grid[i][j] = 0
        self.part_of_island(grid,i,j+1)
        self.part_of_island(grid,i,j-1)
        self.part_of_island(grid,i+1,j)
        self.part_of_island(grid,i-1,j)


# solution 2, BFS - index conversion 

from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(grid,i,j)
                    islands += 1
        return islands
        
    def bfs(self,grid,x,y):
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        xbias = [0,-1,1,0]
        ybias = [-1,0,0,1]
        queue.append(x*n + y)
        grid[x][y] = 0 
        while queue:
            for _ in range(len(queue)):
                index = queue.popleft()
                x = index // n 
                y = index % n 
                for i in range(len(xbias)):
                    new_x = x + xbias[i]
                    new_y = y + ybias[i]
                    if new_x not in range(len(grid)):
                        continue 
                    if new_y not in range(len(grid[0])):
                        continue
                    if grid[new_x][new_y] == 0:
                        continue 
                    queue.append(new_x*n + new_y)
                    grid[new_x][new_y] = 0 
        


# solution3, BFS - using [i][j]

class Solution2:
    def numIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)
                    islands += 1
        return islands  
        
    def bfs(self, grid, x, y):
        queue = deque([(x, y)]) # append queue and mark visited sycn
        grid[x][y] = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]: # 下上左右
                    next_x = x + delta_x
                    next_y = y + delta_y
                    if next_x not in range(len(grid)):
                        continue
                    if next_y not in range(len(grid[0])):
                        continue
                    if grid[next_x][next_y] == 0:
                        continue
                    queue.append((next_x, next_y))
                    grid[next_x][next_y] = 0

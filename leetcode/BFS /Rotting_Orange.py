-from typing import List
from collections import deque 
class Solution:


    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        xBias = [0,0,1,-1]
        yBias = [1,-1,0,0]
        if(grid is None or len(grid) == 0):
            return -1
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        
        # check on how many fresh oranges are in the grid, and append rotting oranges in the queue 
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    fresh += 1
                elif(grid[i][j] == 2):
                    queue.append(i*n + j)
                    
    
        minute = 0 
        while(len(queue) != 0 and fresh != 0):
            size = len(queue)
            for i in range(size):
                index = queue.popleft()
                x = index//n
                y = index % n 
                for j in range(len(xBias)):
                    newX = x + xBias[j]
                    newY = y + yBias[j]
                    if(self.valid(grid,newX,newY)):
                        # check if there is good orange at the index 
                        fresh -= 1
                        queue.append(newX*n + newY) #queue append nearby good orange
                        grid[newX][newY] = 2 # turn good orange into rotting orange
            minute += 1
        
        return (minute if fresh == 0 else -1)
        
    def valid(self, grid, x, y):
        # first check if it is inside of the box, if not return false
        if x < 0 or y < 0 or x>(len(grid)-1) or y>(len(grid[0])-1):
            return False
        # if inside of the box, and if it is a good orange 
        if grid[x][y] == 1:
            return True
        #if it's inside of the box and is not a good orange/ no orange 
        return False
        
        

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
                    
                        
            
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        
        def dfs(y,x):
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid)  or grid[y][x] != "1":
                return
            
        
        
            grid[y][x] = "0"
            
            
            
            dfs(y,x+1)
            dfs(y,x-1)
            dfs(y+1,x)
            dfs(y-1,x)
            
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":

                    dfs(i,j)
                    count += 1
        
        return count
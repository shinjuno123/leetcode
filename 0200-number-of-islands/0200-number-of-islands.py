class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x, y):
            if y > len(grid) - 1 or y < 0 or x > len(grid[0]) - 1 or x < 0 or grid[y][x] == "0":
                return
            
            grid[y][x] = "0"
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            
        
        cnt = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(j, i)
                    cnt += 1
                    
        
        return cnt
        
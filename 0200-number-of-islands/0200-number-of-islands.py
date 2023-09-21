class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        def helper(i,j):
            if(i,j) in visited:
                return 0
            if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0'):
                return 0
            visited.add((i,j))
            helper(i-1,j)
            helper(i+1,j)
            helper(i,j-1)
            helper(i,j+1)
            return 1
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1'):
                    res+=helper(i,j)
        return res
                    

        
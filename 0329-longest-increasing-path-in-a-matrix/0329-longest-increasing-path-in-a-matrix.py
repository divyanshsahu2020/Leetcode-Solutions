class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo={}
        def helper(r, c, pre):
            if r < 0 or c < 0 or r == len(matrix) or c == len(matrix[0]) or matrix[r][c] <= pre:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            res = 0
            res = max(res, helper(r + 1, c, matrix[r][c]))
            res = max(res, helper(r, c + 1, matrix[r][c]))
            res = max(res, helper(r - 1, c, matrix[r][c]))
            res = max(res, helper(r, c - 1, matrix[r][c]))
            memo[(r,c)]= res+1
            return res+1
        fres = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                fres = max(fres, helper(i, j, -1))

        return(fres)



        
            

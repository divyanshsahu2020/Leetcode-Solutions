import numpy as np
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        arr=np.array(grid)
        return(len(arr[arr<0]))
        
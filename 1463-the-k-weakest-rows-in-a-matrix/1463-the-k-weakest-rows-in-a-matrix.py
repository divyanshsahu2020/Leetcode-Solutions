class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res=[]
        for i in range(len(mat)):
            res.append((sum(mat[i]),i))
        res.sort()
        fres=[]
        for a,b in res:
            fres.append(b)
        return fres[:k]
        
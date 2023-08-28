class Solution:
    def removeStars(self, s: str) -> str:
        arr=[]
        for i in s:
            if(i=='*' and len(arr)>0):
                arr.pop()
            else:
                arr.append(i)
        res="".join(arr)
        return res

            
        
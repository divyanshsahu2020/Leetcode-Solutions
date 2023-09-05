class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def helper(s,subseq):
            i1,i2=0,0
            while i1<len(s) and i2<len(subseq):
                if(s[i1]==subseq[i2] and i1 not in removed):
                    i1+=1
                    i2+=1
                else:
                    i1+=1
            return i2==len(subseq)
        
        l,r=0,len(removable)-1
        res=0
        while l<=r:
            mid=(l+r)//2
            removed=set(removable[:mid+1])
            if helper(s,p):
                l=mid+1
                res=max(res,mid+1)
            else:
                r=mid-1

        return res

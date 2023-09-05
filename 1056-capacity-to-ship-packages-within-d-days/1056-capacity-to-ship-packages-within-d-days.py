class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def cap(capacity):
            s=0
            count=1
            for i in weights:
                if(s+i<=capacity):
                    s=s+i
                else:
                    count+=1
                    s=i
            if(count<=days):
                return True
            else:
                return False
        l=max(weights)
        r=sum(weights)
        res=float('inf')
        while l<=r:
            mid=l+((r-l)//2)
            if(cap(mid)):
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res
    
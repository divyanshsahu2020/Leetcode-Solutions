class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        digits={}
        for i in arr:
            temp=i
            count=0
            while i:
                count+=i&1
                i=i>>1
            if count in digits:
                digits[count].append(temp)
            else:
                digits[count]=[temp]
        res=[]
        t=list(digits.keys())
        t.sort()
        for i in t:
            res.extend(digits[i])
        return res


        
class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l=len(s)-1
        su=d[s[-1]]
        for i in range(l):
            if(d[s[i]]<d[s[i+1]]):
                su=su-d[s[i]]
            else:
                su=su+d[s[i]]
        return su
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s)>len(t)):
            return False
        l1=0
        l2=0
        while l1<len(s) and l2<len(t):
            if(s[l1]==t[l2]):
                l1+=1
                l2+=1
            else:
                l2+=1
        if(l1==len(s)):
            return True
        return False
        
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo={}
        if len(s1)+len(s2)!=len(s3):
            return False
        def helper(inde1,inde2,inde3):
            if (inde1,inde2,inde3) in memo:
                return memo[(inde1,inde2,inde3)]
            if(inde3==len(s3)):
                return True
            res=False
            if inde1==len(s1):
                return s2[inde2:]==s3[inde3:]
            if inde2==len(s2):
                return s1[inde1:]==s3[inde3:]

            if s1[inde1]!=s3[inde3] and s2[inde2]!=s3[inde3]:
                return False
            elif (s1[inde1]==s2[inde2]==s3[inde3]):
                res=res or helper(inde1+1,inde2,inde3+1) or helper(inde1,inde2+1,inde3+1)
            elif s1[inde1]==s3[inde3]:
                res=res or helper(inde1+1,inde2,inde3+1)
            elif s2[inde2]==s3[inde3]:
                res=res or helper(inde1,inde2+1,inde3+1)
            memo[(inde1,inde2,inde3)]= res
            return memo[(inde1,inde2,inde3)]
        return helper(0,0,0)
            
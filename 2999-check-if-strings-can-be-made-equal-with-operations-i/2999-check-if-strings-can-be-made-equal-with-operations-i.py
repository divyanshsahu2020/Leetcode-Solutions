class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        s1=[i for i in s1]
        s2=[i for i in s2]
        if not s1[0]==s2[0]:
            s1[0],s1[2]=s1[2],s1[0]
        if not s1[1]==s2[1]:
            s1[1],s1[3]=s1[3],s1[1]

        return s1==s2
        

            

        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=strs[0]
        count=0
        for i in range(len(x)):
            temp=x[i]
            for j in strs:
                if i>=len(j):
                    return x[:count]
                if not(j[i]==temp):
                    return x[:count]
            count+=1
        return x[:count]
                    

        
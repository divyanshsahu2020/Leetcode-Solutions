class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=('a','e','i','o','u')
        res=0
        curr=0
        l=0
        r=0
        while r<len(s):
            win_len=r-l+1
            if(win_len>k):
                
                if(s[l] in vowels):
                    curr-=1
                l+=1
                
            if(s[r] in vowels):
                curr+=1
            r+=1
            res=max(res,curr)
        return res

        
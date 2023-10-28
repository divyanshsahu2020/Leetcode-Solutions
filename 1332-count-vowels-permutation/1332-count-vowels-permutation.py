class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels={
            'a':['e'],
            'e':['a','i'],
            'i':['a','e','o','u'],
            'o':['i','u'],
            'u':['a']
        }
        memo={}

        def helper(curr,l):
            if (curr,l) in memo:
                return memo[(curr,l)]
            if l==0:
                return 1
            if l==1:
                return len(vowels[curr])
            res=0
            for i in vowels[curr]:
                res+=helper(i,l-1)
            memo[(curr,l)]= res
            return res
        fres=0
        for i in vowels.keys():
            fres+=helper(i,n-1)
        return fres%(10**9 + 7)
            
            
            
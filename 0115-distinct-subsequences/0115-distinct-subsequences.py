class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}
        def helper(s_inde,t_inde):
            if t_inde==len(t):
                return 1
            if s_inde==len(s):
                return 0
            if (s_inde, t_inde) in memo:
                return memo[(s_inde, t_inde)]
            pick=0
            if s[s_inde]==t[t_inde]:
                pick=helper(s_inde+1,t_inde+1)
            notpick=(helper(s_inde+1,t_inde))
            memo[(s_inde, t_inde)]= pick+notpick
            return memo[(s_inde, t_inde)]
        return helper(0,0)

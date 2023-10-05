class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        n=len(nums)
        freq=Counter(nums)
        res=[]
        for i,j in freq.items():
            if j>n//3:
                res.append(i)
        return res
        
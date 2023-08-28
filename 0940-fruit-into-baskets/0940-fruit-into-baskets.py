class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        first=[None,0]
        second=[None,0]
        l,r=0,0
        res=0
        while r<len(nums):
            ele=nums[r]
            if(ele==first[0] or first[0]==None):
                if(first[0]==None):
                    first[0]=ele
                    first[1]=1
                else:
                    first[1]+=1
            elif(ele==second[0] or second[0]==None):
                if(second[0]==None):
                    second[0]=ele
                    second[1]=1
                else:
                    second[1]+=1
            else:

                while not(first[1]==0 or second[1]==0):
                    temp=nums[l]
                    if(temp==first[0]):
                        first[1]-=1
                    else:
                        second[1]-=1
                    l+=1
                if(first[1]==0):
                    first[0]=ele
                    first[1]=1
                else:
                    second[0]=ele
                    second[1]=1
            res = max(res, first[1] + second[1])
            r+=1
        return (res)
                
                            
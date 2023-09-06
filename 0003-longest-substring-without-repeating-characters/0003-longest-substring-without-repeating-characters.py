class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=""
        count=-1
        for i in s:
            if i in temp:
                if(count<len(temp)):
                    count=len(temp)
                ind=temp.index(i)
                temp=temp+i
                temp=temp[ind+1:]
            else:
                temp=temp+i
        if(count<len(temp)):
            count=len(temp)
        return int(count)


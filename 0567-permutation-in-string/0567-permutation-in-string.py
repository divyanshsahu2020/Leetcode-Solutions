class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        words={}
        for i in s1:
            if(i in words):
                words[i]+=1
            else:
                words[i]=1
        l=0
        while l<len(s2):
            ele=s2[l]
            if(ele in words):
                temp=l
                if((temp+len(s1))>len(s2)):
                    return False
                s=s2[temp:temp+len(s1)]
                words2={}
                for ele in s:
                    if(ele in words2):
                        words2[ele]+=1
                    else:
                        words2[ele]=1
                if(words==words2):
                    return True
            l+=1
        return False
            
            

        
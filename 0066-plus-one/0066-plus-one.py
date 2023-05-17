class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        arr=[]
        for i in digits:
            num=num*10+i
        num=num+1
        for i in str(num):
            arr.append(int(i))
        return arr
        

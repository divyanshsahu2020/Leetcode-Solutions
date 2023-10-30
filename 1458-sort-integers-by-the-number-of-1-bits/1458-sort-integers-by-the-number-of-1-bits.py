class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        digits=[]
        for i in arr:
            digits.append((bin(i).replace('0b','').count('1'),i))
        digits.sort()
        for i in range(len(digits)):
            digits[i]=digits[i][1]
        return digits

        
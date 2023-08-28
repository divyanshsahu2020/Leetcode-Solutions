class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        arr=deque()
        brac={'(': ')', '{':'}', '[':']'}
        if not (s[0] in brac):
            return False
        for i in s:
            if i in brac:
                arr.append(i)
            else:
                if(len(arr)==0):
                    return False
                if(brac[arr[-1]]==i):
                    arr.pop()
                else:
                    return False
        return len(arr)==0

        
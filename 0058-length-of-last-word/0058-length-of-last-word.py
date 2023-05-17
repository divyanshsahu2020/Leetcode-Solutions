class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip(' ')
        t=[i for i in s.split(' ')]
        return len(t[-1])
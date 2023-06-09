class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        first=letters[0]
        letters=sorted(letters)
        for i in letters:
            if(i>target):
                return i
        return first
        
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        for i in text.split(' '):
            if not any(letter in set(brokenLetters) for letter in i):
                count+=1
        return count

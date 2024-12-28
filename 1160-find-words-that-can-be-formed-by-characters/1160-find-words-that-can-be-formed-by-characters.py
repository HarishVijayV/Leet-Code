class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        a=Counter(chars)
        c=0
        for i in words:
            b=Counter(i)
            if all(b[j]<=a[j] for j in b):
                c+=len(i)
        return c
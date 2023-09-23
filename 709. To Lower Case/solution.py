class Solution:
    def toLowerCase(self, s: str) -> str:
        c=''
        for char in s:
            if 'A'<=char<='Z':
                c+=chr(ord(char)+32)
            else:
                c+=char
        return c
            
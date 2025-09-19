class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sum=0
        sentence=str(set(sentence))
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        s=set(sentence)
        for i in alphabets:
            if i in s:
                continue
            else:
                return False
        return True
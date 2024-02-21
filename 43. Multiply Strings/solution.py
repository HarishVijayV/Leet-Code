class Solution:
    def intmaker(self,s:str) -> int:
        buff=0
        for i in s:
            buff*=10
            buff+=int(i)
        return buff

    
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.intmaker(num1)*self.intmaker(num2))
        
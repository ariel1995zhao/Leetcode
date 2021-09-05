class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry > 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result.append(str((x + y + carry) % 10))
            carry = (x + y + carry) // 10
            i -= 1
            j -= 1
     
        return "".join(result[::-1])
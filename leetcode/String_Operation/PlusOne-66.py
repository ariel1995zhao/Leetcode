class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return 
        reverse = digits[::-1]
        carry = 1
        for i in range(len(digits)):
            reverse[i] = reverse[i] + carry 
            if reverse[i] >= 10:
                reverse[i] = reverse[i] - 10
                if i == len(reverse) -1 and reverse[i] == 0:
                    reverse.append(1)
                    return reverse[::-1]
            else:
                return reverse[::-1]


## solution 2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        
        for i in range(n-1, -1, -1):
            
            if digits[i] == 9:
                digits[i] = 0
                    
            else:
                digits[i] += 1
                
                return digits
            
        return [1] + digits
        
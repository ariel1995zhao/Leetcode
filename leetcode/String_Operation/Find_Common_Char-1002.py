class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ## solution 1:
        ## use first subarry as reference, take each letter from there, compare each letter one by one with the rest subarrays 
        ## first set valid to be True, if not in subarrays, set Valid to be False. If in subarray, earse it, and append it to result
        ## "label","roller"
        ##  b
        ## b in "label", so valid stays True, and earse b in "label", which becomes to "lael".
        ## Then compare b with "roller", b not in roller, then set valid to be False. Do not append 
        if not words:
            return []
        reference = words[0]
        result = []
        for letter in reference:
            valid = True
            for i in range(1,len(words)):
                if letter not in words[i]:
                    valid = False 
                    break 
                else:
                    words[i] = words[i].replace(letter,"",1)
                
            if valid:
                result.append(letter)
        return result
        
                
                

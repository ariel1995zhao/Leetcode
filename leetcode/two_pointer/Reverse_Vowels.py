class Solution:
    
    ## two pointer, one start from left, one start from the end 
    ## if not vowels, then left + 1, if not vowels, then right -1 
    ## if until find two vowels, then swap.
    
    ## h e l l o 
    ## L
    ##         R
    def reverseVowels(self, s: str) -> str:
        if not s:
            return 
        word_set = {'a','e','i','o','u',"A","E","I","O","U"}
        left = 0 
        right = len(s)-1
        s_list = [word for word in s]
        while left < right-1:
            if s_list[left] not in word_set:
                left += 1
            if s_list[right] not in word_set:
                right -=1
            if s_list[left] in word_set and s_list[right] in word_set:
                #swithc 
                s_list[left],s_list[right] = s_list[right],s_list[left]
                right -=1 
                left += 1
        return "".join(s_list)
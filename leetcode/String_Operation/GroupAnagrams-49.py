## Group Anagrams 



## Use data structure: Dictionary, keys: Tuples of letters, values: array of words 

## first sort each word in strs list, and make each letter of word in a tuple, and then check if it's in dictionary 

## if it's in dictionary, then make the value append the word.

## if not in dictionary, then make the key as tuple of word list, and value as the array of words 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictSets = {}
        
        for element in strs:
            fSet = tuple(sorted(element))
            if fSet in dictSets:
                dictSets[fSet].append(element)
            else:
                dictSets[fSet] = [element]
        return(list(dictSets.values()))


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
            return None

        anagrams  = defaultdict(list)

        for word in strs:

            count = [0]*26
            for char in word:
                idx = ord(char) -97
                count[idx]+=1
            key = tuple(count)
            anagrams[key].append(word)
        return list(anagrams.values())



                
        

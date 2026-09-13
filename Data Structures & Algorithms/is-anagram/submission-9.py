from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = defaultdict(int)
        dic_t = defaultdict(int)

        if len(s) != len(t): return False
        else:

            for i in range(len(s)):
                print(s[i])
                dic_s[s[i]]+=1
                dic_t[t[i]]+=1
        
        return dic_s == dic_t
        
        
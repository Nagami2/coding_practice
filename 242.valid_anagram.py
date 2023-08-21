class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # compare the two anagrams 
        if len(s) != len(t):
            return False

        count_s, count_t ={},{}

        for c in s:
            count_s[c] = 1+ count_s.get([c],0)
        
        for c in t:
            count_t[c] = 1+ count_t.get([c],0)
        
'''
        for i in range(len(s)):
            count_s[s[i]] = 1+ count_s.get(s[i],0)
            count_t[t[i]] = 1+ count_t.get(t[i],0)
            '''
        return count_s == count_t  
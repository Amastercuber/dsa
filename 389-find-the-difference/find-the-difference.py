class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count_s = {}
        for ch in s:
            if ch not in count_s:
                count_s[ch] = 1
            else:
                count_s[ch] += 1

        count_t = {}
        for ch in t:
            if ch not in count_t:
                count_t[ch] = 1
            else:
                count_t[ch] += 1
        

        for ch in t:
            if ch not in count_s or count_s[ch] != count_t[ch]:
                return ch
        
        
        
        
        
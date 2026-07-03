class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strArr = []
        for char in s:
            if char.isalnum():
                strArr.append(char.lower()) 
        
        str = "".join(strArr)
        l, r = 0, len(str)-1

        while l< r:
            if str[l] != str[r]:
                return False
            l += 1
            r -= 1
        return True
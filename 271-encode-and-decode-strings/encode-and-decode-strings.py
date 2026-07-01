class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        output = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            output.append(s[j+1:j + 1 + length])
            i = j + 1 + length
        return output
        

                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
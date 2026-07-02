class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        output = []
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                product *= n
        if zeros > 1:
            return [0] * len(nums)
        
        for n in nums:
            if zeros != 0:
                if n == 0:
                    output.append(product)
                else:
                    output.append(0)
            else:
                output.append(product//n)
            
        return output
        
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 0
        for num in nums:
            if write == 0 or num != nums[write - 1]:
                nums[write] = num
                write += 1
        return write
        
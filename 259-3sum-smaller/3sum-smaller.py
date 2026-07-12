class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        count = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < target:
                    # All triplets using indices from left+1 through right
                    # as the third value are also valid.
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count
        
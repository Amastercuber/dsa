class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        left, right = 0, len(nums) - 1

        while left <= right:
            if left == right:
                output.append(nums[left] * nums[right])
            else:
                l = nums[left] * nums[left]
                r = nums[right] * nums[right]
                if l < r:
                    output.append(l)
                    output.append(r)
                else:
                    output.append(r)
                    output.append(l)
            left += 1
            right -= 1
        return sorted(output)
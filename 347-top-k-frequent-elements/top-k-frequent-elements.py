class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts={}
        freq = [[] for i in range(len(nums) + 1)]

        # get counts
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
        
        for val, count in counts.items():
            freq[count].append(val)
        output = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
        
        
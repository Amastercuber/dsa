#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_min_sublist_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#

def find_min_sublist_sum(nums, k):
    # Write your code here
    if len(nums) < k:
        return 0
    left, right = 0,k
    sums = []
    while right <= len(nums):
        sumi = 0
        for i in range(left,right):
            sumi += nums[i]
        sums.append(sumi)
        left += 1
        right += 1
    return min(sums)
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'find_pair_sum' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER target
#

def find_pair_sum(s, target):
    # Write your code here
    left = 0
    right = 1
    while right < len(s):
        if int(s[left]) + int(s[right]) == target:
            return True
        left += 1
        right += 1
    return False
# https://leetcode.com/problems/kth-missing-positive-number/

# Every time we iterate through the loop, we can figure out how many missing number we just go through
# There will be 3 cases:
# Case 1: the next number is actually the next number in the int list
# Case 2: the remaining number we have to traverse through is between the current number and the next number
# Case 3: the rest

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        cur = 0
        rem = k
        for num in arr:
            gap = num - cur
            if gap == 1:
                cur = num
            elif gap - 1 >= rem:
                return cur + rem
            else:
                rem = rem - gap + 1 
                cur = num
        return cur + rem 
        
# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        list = {}
        for num in nums:
            if num in list:
                return True
            else:
                list[num] = 1
        return False
        
        
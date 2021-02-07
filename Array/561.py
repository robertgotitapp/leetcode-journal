class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        sum = 0
        for i in range(len(sorted_nums) / 2 ):
            sum += min(sorted_nums[2 * i], sorted_nums[2* i + 1])
        return sum
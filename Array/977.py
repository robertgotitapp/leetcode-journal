class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squaredArr = []
        for num in nums:
            squaredArr.append(num ** 2)
        return squaredArr.sort()
        
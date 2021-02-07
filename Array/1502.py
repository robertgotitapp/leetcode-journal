class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sorted_arr = sorted(arr)
        diff = sorted_arr[1] - sorted_arr[0]
        for i in range(1, len(sorted_arr) - 1):
            if sorted_arr[i + 1] - sorted_arr[i] != diff:
                return False
        return True
            
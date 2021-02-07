class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_heights = sorted(heights)
        swap_count = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                swap_count += 1
        return swap_count
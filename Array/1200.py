class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        # idea is to sort the array first then calculate min difference of 2 consecutive numbers
        sortedArray = sorted(arr)
        minDiff = sys.maxint
        list = []
        for i in range(len(sortedArray) - 1):
            diff = sortedArray[i] - sortedArray[i + 1]
            absDiff = abs(diff)
            if absDiff == minDiff:
                list.append([sortedArray[i], sortedArray[i + 1]] if diff < 0 else [sortedArray[i+1], sortedArray[i]])
            elif absDiff < minDiff:
                minDiff = absDiff
                list = [[sortedArray[i], sortedArray[i + 1]]] if diff < 0 else [[sortedArray[i+1], sortedArray[i]]]
        return list
            
        
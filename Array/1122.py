class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
            
        arr3 = []
        res = []
        for num in arr1:
            if num not in arr2:
                arr3.append(num)
            else:
                res.append(num)
        start = 0
        temp = 0
        for num in arr2:
            for i in range(start, len(res)):
                if res[i] == num:
                    if start != i:
                        temp = res[start]
                        res[start] = num
                        res[i] = temp
                    start += 1
        for num in sorted(arr3):
            res.append(num)
        return res
            
                    
                    
        
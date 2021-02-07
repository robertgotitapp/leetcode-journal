class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        def getMinIndexInList (num_list):
            min_num = sys.maxint
            min_index = -1
            for i in range(len(num_list)):
                if num_list[i] < min_num:
                    min_num = num_list[i]
                    min_index = i
            return min_index
        
        def getMaxIndexinCol (matrix, col_index, row_length):
            max_num = -sys.maxint - 1
            max_index = -1
            for i in range(row_length):
                if matrix[i][col_index] > max_num:
                    max_num = matrix[i][col_index]
                    max_index = i
            return max_index
        
        result = []
        dict = {}
        row_length = len(matrix)
        col_length = len(matrix[0])
        for row_index in range(row_length):
            dict[row_index] = getMinIndexInList(matrix[row_index])
            
        for col_index in range(col_length):
            max_index = getMaxIndexinCol(matrix, col_index, row_length)
            if dict[max_index] == col_index:
                result.append(matrix[max_index][col_index])
        return result
        
            
        
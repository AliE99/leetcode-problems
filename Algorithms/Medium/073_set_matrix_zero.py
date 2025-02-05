class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_columns = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_columns.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zero_rows or col in zero_columns:
                    matrix[row][col] = 0



matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(Solution().setZeroes(matrix))

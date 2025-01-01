class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            top = left
            buttom = right
            for i in range(right - left):
                tmp = matrix[top][left + i]

                matrix[top][left + i] = matrix[buttom - i][left]

                matrix[buttom - i][left] = matrix[buttom][right - i]

                matrix[buttom][right - i] = matrix[top + i][right]

                matrix[top + i][right] = tmp

            left += 1
            right -= 1


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().rotate(matrix))

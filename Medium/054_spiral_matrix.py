class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        first_row = 1
        first_col = 0
        last_row = len(matrix) - 1
        last_col = len(matrix[0]) - 1

        r = c = 0
        result: list[int] = []
        max_len = len(matrix) * len(matrix[0])
        while len(result) < max_len:

            # Move Right
            while c <= last_col and len(result) < max_len:
                result.append(matrix[r][c])
                c += 1
            c -= 1
            r += 1
            last_col -= 1

            # Move Down
            while r <= last_row and len(result) < max_len:
                result.append(matrix[r][c])
                r += 1
            r -= 1
            c -= 1
            last_row -= 1

            # Move Left
            while c >= first_col and len(result) < max_len:
                result.append(matrix[r][c])
                c -= 1
            c += 1
            r -= 1
            first_col += 1

            # Move Up
            while r >= first_row and len(result) < max_len:
                result.append(matrix[r][c])
                r -= 1
            r += 1
            c += 1
            first_row += 1

        return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(Solution().spiralOrder(matrix))

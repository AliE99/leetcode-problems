class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        first_column = [row[0] for row in matrix]
        row = self.__find_the_row(column=first_column, target=target)
        return self.__find_target_in_row(row=matrix[row], target=target)

    def __find_the_row(self, column: list[int], target: int) -> int:
        low = 0
        high = len(column) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == column[mid]:
                return mid
            elif target > column[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return low - 1

    def __find_target_in_row(self, row: list[int], target: int) -> bool:
        low = 0
        high = len(row) - 1

        while high >= low:
            mid = (high + low) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13

print(Solution().searchMatrix(matrix, target))

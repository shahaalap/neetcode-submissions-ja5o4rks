class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix), len(matrix[0])
        i , j = 0, m * n - 1

        while i <= j:
            mid =  i + ((j - i) // 2) 
            x, y, data = 0 , 0, 0
            if mid < len(matrix[0]):
                y = mid
            else:
                x = mid // n
                y = mid % n
            data = matrix[x][y]

            if data == target:
                return True
            elif data > target:
                j = mid - 1
            else:
                i = mid + 1

        return False

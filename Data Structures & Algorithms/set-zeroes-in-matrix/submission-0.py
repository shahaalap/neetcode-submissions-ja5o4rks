class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows , cols = len(matrix), len(matrix[0])
        rowzero, colzero = [False] * rows, [False] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowzero[i] = True
                    colzero[j] = True

        
        for i in range(rows):
            for j in range(cols):
                if rowzero[i] or colzero[j]:
                    matrix[i][j] = 0
                    
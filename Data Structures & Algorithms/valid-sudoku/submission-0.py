class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                curitem = board[i][j]
                if curitem == '.':
                    continue

                if curitem in rows[i] or curitem in cols[j] or curitem in boxes[(i//3, j//3)]:
                    return False
                
                rows[i].add(curitem)
                cols[j].add(curitem)
                boxes[(i//3, j//3)].add(curitem)

        
        return True



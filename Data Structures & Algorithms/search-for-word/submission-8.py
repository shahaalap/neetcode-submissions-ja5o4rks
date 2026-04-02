class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l, w = len(board), len(board[0])
        visited = [[False] * w for _ in range(l)]

        def dfs(i, j , c):
            if c == len(word):
                return True

            if i < 0 or i >= l or j < 0 or j >= w:
                return False

            if visited[i][j]:
                return False

            

            if board[i][j] == word[c]:   
                visited[i][j] = True             
                ans1 = dfs(i + 1, j, c + 1) 
                ans2 = dfs(i - 1, j, c + 1) 
                ans3 = dfs(i, j + 1, c + 1) 
                ans4 = dfs(i, j - 1, c + 1)

                if not all([ans1, ans2, ans3, ans4]):
                    visited[i][j] = False
                
                if ans1 or ans2 or ans3 or ans4:
                    return True   
                else:
                    return False             
            else:
                return False
        
        for i in range(l):
            for j in range(w):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False






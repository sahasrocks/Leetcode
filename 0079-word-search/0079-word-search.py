class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        path=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] or (r,c) in path):
                return False
            path.add((r,c))
            res = dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False                

        
        
        # rows=len(board)
        # cols=len(board[0])
        # path=set()
        # def dfs(r,c,i):
        #     if i==len(word):
        #         return True
        #     if (r<0 or c<0 or r>=rows or c>=cols or word[i] !=board[r][c] or (r,c) in path):
        #         return False
        #     path.add((r,c))
        #     res=dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)
        #     path.remove((r,c))
        #     return res
        # for r in range(rows):
        #     for c in range(cols):
        #         if dfs(r,c,0):
        #             return True
        # return False                        
        
        
        # rows=len(board)
        # cols=len(board[0])
        # path=set()

        # def dfs(r,c,i):
        #     if i==len(word):
        #         return True
        #     if ( r<0 or c<0 or r>=rows or c>=cols or word[i] != board[r][c] or (r,c) in path ):
        #         return False
        #     path.add((r,c))
        #     res = dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)
        #     path.remove((r,c))
        #     return res
        # for r in range(rows):
        #     for c in range(cols):
        #         if dfs(r,c,0):
        #             return True
        # return False                

        
        
        
        
        
        
        
        
        
        # def search(board, x, y, word, visited=set()):
        #     if word == '':
        #         return True
        #     for i, j in [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]:
        #         if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in visited and board[i][j] == word[0] \
        #         and search(board, i, j, word[1:], visited | {(x, y)}):
        #             return True
        #     return False
        
        # if not board or not board[0]:
        #     return False
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] == word[0] and search(board, i, j, word[1:]):
        #             return True
        # return False
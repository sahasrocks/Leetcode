class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square=defaultdict(set)
        rows=defaultdict(set)
        cols=defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True            

        
        
        
        
        
        
        
        
        
        
        
        
        
        # boardMap = collections.defaultdict(list)
        # for x in range(9):
        #     for y in range(9):
        #         char = board[x][y]
        #         if char != '.': 
        #             if char in boardMap:
        #                 for pos in boardMap[char]:
        #                     if (pos[0]== x) or (pos[1] == y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3):
        #                         return False
        #             boardMap[char].append((x,y))
   
        # return True
        
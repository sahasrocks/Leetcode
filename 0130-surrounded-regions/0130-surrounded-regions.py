class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols=len(board),len(board[0])
        def dfs(r,c):
            if (r<0 or c<0 or r==rows or c==cols or board[r][c] !="O"):
                return
            board[r][c]="T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r in [0,rows-1] or c in [0,cols-1]):
                    dfs(r,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"            


        # def dfs(r,c):
        #     if (r<0 or c<0 or r==rows or c==cols or board[r][c] !="O"):
        #         return
        #     board[r][c]="T"
        #     dfs(r+1,c)
        #     dfs(r-1,c)
        #     dfs(r,c+1)
        #     dfs(r,c-1)
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c]=="O" and (r in [0,rows-1] or c in [0,cols-1]):
        #             dfs(r,c)
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c]=="O":
        #             board[r][c]="X"
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c]=="T":
        #             board[r][c]="O"                                
        



    #bfs sol
        # q=deque()
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c]=="O" and (r in [0,rows-1] or c in [0,cols-1]):
        #             q.append((r,c))
        # while q:
        #     r,c=q.popleft()
        #     if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
        #         board[r][c] = "T"
        #         # Add neighbors
        #         q.append((r + 1, c))
        #         q.append((r - 1, c))
        #         q.append((r, c + 1))
        #         q.append((r, c - 1))
        #  # Step 3️⃣: Flip inner 'O's to 'X'
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] == "O":
        #             board[r][c] = "X"

        # # Step 4️⃣: Restore safe 'T's to 'O'
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] == "T":
        #             board[r][c] = "O"        



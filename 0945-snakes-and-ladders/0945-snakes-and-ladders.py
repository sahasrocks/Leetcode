class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        length = len(board)

        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]

        q = deque()
        q.append([1, 0])  # (square, moves)
        visit = set([1])  # mark starting square visited

        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i

                # ✅ Prevent out-of-bounds
                if nextSquare > length * length:
                    continue

                r, c = intToPos(nextSquare)

                # if ladder/snake
                if board[r][c] != -1:
                    nextSquare = board[r][c]

                # reached the end
                if nextSquare == length * length:
                    return moves + 1

                # enqueue next move
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])

        return -1
         

    # class Solution:
    # def snakesAndLadders(self, board: List[List[int]]) -> int:
    #     n = len(board)

    #     def intToPos(square):
    #         r = (square - 1) // n
    #         c = (square - 1) % n
    #         if r % 2 == 1:
    #             c = n - 1 - c
    #         r = n - 1 - r
    #         return r, c

    #     q = deque([(1, 0)])
    #     visit = set()

    #     while q:
    #         square, moves = q.popleft()

    #         for i in range(1, 7):
    #             nextSquare = square + i
    #             r, c = intToPos(nextSquare)
    #             if board[r][c] != -1:
    #                 nextSquare = board[r][c]

    #             if nextSquare == n * n:
    #                 return moves + 1

    #             if nextSquare not in visit:
    #                 visit.add(nextSquare)
    #                 q.append((nextSquare, moves + 1))

    #     return -1           




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # queue = collections.deque()
        # n = len(board)
        # queue.append((1, 0)) # (label, path_len)
        # visited = set()
        
        # def square_to_idx(val):
        #     row_idx = n - 1 - (val - 1) // n
        #     revert = True if (n - 1 - row_idx) % 2 == 1 else False
        #     col_idx = (val - 1) % n
        #     col_idx = n - 1 - col_idx if revert else col_idx
        #     return row_idx, col_idx
        
        # while queue:
        #     cur_val, path_len = queue.popleft()
        #     visited.add(cur_val)
        #     cur_row, cur_col = square_to_idx(cur_val)
        #     # see a ladder/snake and move
        #     # note this doesn't take an extra step
        #     # so no need to add to the queue
        #     if board[cur_row][cur_col] != -1:
        #         cur_val = board[cur_row][cur_col]
        #     # game ends
        #     # note: cannot use cur_row = row_col == 0 
        #     # as the first row might be reverted
        #     if cur_val == n ** 2:
        #         return path_len
        #     # next move
        #     max_move = min(cur_val + 6, n ** 2)
        #     for dest_val in range(cur_val + 1, max_move + 1):
        #         if dest_val not in visited:
        #             dest_row, dest_col = square_to_idx(dest_val)
        #             queue.append((dest_val, path_len + 1))

        # return -1
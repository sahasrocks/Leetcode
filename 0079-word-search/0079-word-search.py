class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(board, x, y, word, visited=set()):
            if word == '':
                return True
            for i, j in [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]:
                if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in visited and board[i][j] == word[0] \
                and search(board, i, j, word[1:], visited | {(x, y)}):
                    return True
            return False
        
        if not board or not board[0]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and search(board, i, j, word[1:]):
                    return True
        return False
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # declare rows and cols
        # declare dirs for neighbors
        # traverse the board, if "O" on edge of board, change to "T" so we don't mess with it
        # if "O" not on edge of board, append to queue

        # BFS approach
        # pop from queue, make that cell "X", capturing it, then mark as seen
        # check neighbors, if "O" and haven't seen yet, then append to queue

        # one more pass through the grid
        # if equal to "T", change back to "O"

        rows = len(board)
        cols = len(board[0])
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    q.append((r,c))
        
        while q:
            r, c = q.popleft()

            if board[r][c] == 'O':
                board[r][c] = 'T'

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                        q.append((nr, nc))
        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'


        
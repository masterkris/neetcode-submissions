class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()

        # put all "O" cells in queue
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or
                c == 0 or c == cols - 1) and board[r][c] == "O":
                    q.append([r,c])
        
        # pop from queue, if O make T, push neighbors into queue
        while q:
            r, c = q.popleft()
            if board[r][c] == "O":
                board[r][c] = "T" # make temporarily
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < rows and nc < cols:
                        q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O" # the surrounded regions 



        

